"""FastAPI main application entry point."""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import get_settings
from .database import init_db
from .api.routes import tasks_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan handler for startup/shutdown events."""
    # Startup - try to init DB but don't crash if it fails
    try:
        logger.info("Initializing database connection...")
        await init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        # Don't crash - allow app to start so health check can report status
    yield
    # Shutdown (nothing to clean up)


app = FastAPI(
    title="Todo App API",
    description="Phase II Full-Stack Todo Web Application API",
    version="1.0.0",
    lifespan=lifespan,
)

# Configure CORS - allow all origins for now, we'll restrict later
# Include both the settings origins and common Vercel patterns
cors_origins = settings.cors_origins_list + [
    "https://frontend-iota-six-87.vercel.app",
    "https://*.vercel.app",
]
logger.info(f"CORS origins: {cors_origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for debugging
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(tasks_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/api/test")
async def test_endpoint() -> dict[str, str]:
    """Test endpoint to verify API is working."""
    return {"message": "API is working!", "cors": "enabled"}
