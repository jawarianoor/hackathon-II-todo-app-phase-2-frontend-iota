"""Database connection and session management."""

import logging
import ssl
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from .config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


def get_clean_database_url() -> str:
    """Clean and format DATABASE_URL for asyncpg."""
    url = settings.database_url

    # Ensure it uses asyncpg driver
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://", 1)

    # Remove query parameters that conflict with our SSL setup
    if "?" in url:
        base_url = url.split("?")[0]
        url = base_url

    # Log sanitized URL (hide password)
    sanitized = url.split("@")[1] if "@" in url else url
    logger.info(f"Database host: {sanitized}")
    return url


def get_ssl_context():
    """Create SSL context for Neon PostgreSQL connection."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


engine = create_async_engine(
    get_clean_database_url(),
    echo=False,
    future=True,
    connect_args={"ssl": get_ssl_context()},
    pool_pre_ping=True,  # Test connections before using
)

async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def init_db() -> None:
    """Initialize database tables."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency that provides a database session."""
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
