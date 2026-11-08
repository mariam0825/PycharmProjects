from pydantic import BaseModel,Field
from  typing import Optional
from uuid import UUID , uuid4
from datetime import datetime, timezone

class TodoCreate(BaseModel):
    """What the client sends us to create a todo, also known as DTO"""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    """What the client sends us to update a todo (all optional). update DTO"""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(BaseModel):
    """The full todo, as stored and as returned to the client."""
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )