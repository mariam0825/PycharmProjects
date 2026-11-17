from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from models.grocery_list import GroceryItem

class GroceryItemRepository(ABC):

    @abstractmethod
    def add(self, item: GroceryItem) -> GroceryItem:
        ...

    @abstractmethod
    def get(self, item_id: UUID) -> Optional[GroceryItem]:
        ...

    @abstractmethod
    def list(self) -> List[GroceryItem]:
        ...

    @abstractmethod
    def update(
        self, item_id: UUID, data: dict
    ) -> Optional[GroceryItem]:
        ...

    @abstractmethod
    def delete(self, item_id: UUID) -> bool:
        ...
