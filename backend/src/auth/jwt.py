"""JWT token verification for Better Auth tokens."""

from datetime import datetime
from typing import Optional
from uuid import UUID

from jose import JWTError, jwt
from pydantic import BaseModel

from ..config import get_settings


class TokenPayload(BaseModel):
    """Decoded JWT token payload."""

    sub: str  # User ID
    email: Optional[str] = None
    iat: Optional[int] = None
    exp: Optional[int] = None

    @property
    def user_id(self) -> UUID:
        """Get user ID as UUID."""
        return UUID(self.sub)


def verify_token(token: str) -> Optional[TokenPayload]:
    """
    Verify a JWT token and return the payload.

    Args:
        token: The JWT token string

    Returns:
        TokenPayload if valid, None if invalid or expired
    """
    settings = get_settings()

    try:
        payload = jwt.decode(
            token,
            settings.better_auth_secret,
            algorithms=["HS256"],
        )

        # Check expiration
        exp = payload.get("exp")
        if exp and datetime.utcnow().timestamp() > exp:
            return None

        return TokenPayload(**payload)

    except JWTError:
        return None
