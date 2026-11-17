from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone

class GroceryItemCreate(BaseModel):
    """What the client sends  to us to create a grocery item."""
    name: str = Field(..., min_length=1, max_length=200)
    quantity: int = Field(..., gt=0)


class GroceryItemUpdate(BaseModel):
    """What the client sends to us to update a grocery item."""
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    quantity: Optional[int] = Field(None, gt=0)
    purchased: Optional[bool] = None


class GroceryItem(BaseModel):
    """The full grocery item, as stored and returned to the client."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    quantity: int
    purchased: bool = False

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
