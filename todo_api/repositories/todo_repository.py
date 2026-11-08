from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from models.todo import Todo

class TodoRepository(ABC):
    """Contract every repository (list, MongoDB, ...) must follow."""
    @abstractmethod
    def add(self, todo: Todo) -> Todo:
        ...
    @abstractmethod
    def get(self, todo_id: UUID) -> Optional[Todo]:
        ...
    @abstractmethod
    def list(self) -> List[Todo]:
        ...
    @abstractmethod
    def update(self, todo_id: UUID, data: dict) -> Optional[Todo]:
        ...
    @abstractmethod
    def delete(self, todo_id: UUID) -> bool:
        ...