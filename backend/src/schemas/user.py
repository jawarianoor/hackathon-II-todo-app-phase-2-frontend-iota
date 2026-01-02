"""User Pydantic schemas for API requests and responses."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Schema for user registration request."""

    email: EmailStr
    password: str = Field(..., min_length=8)


class UserResponse(BaseModel):
    """Schema for user response data."""

    id: UUID
    email: str
    created_at: datetime

    class Config:
        from_attributes = True
