from typing import List, Optional
from uuid import UUID
from models.grocery_list import GroceryItem
from repositories.grocery_list_repository import GroceryItemRepository

class InMemoryGroceryItemRepository(GroceryItemRepository):
    def __init__(self):
        self._items: List[GroceryItem] = []

    def add(self, item: GroceryItem) -> GroceryItem:
        self._items.append(item)
        return item

    def get(self, item_id: UUID) -> Optional[GroceryItem]:
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    def list(self) -> List[GroceryItem]:
        return self._items

    def update(self, item_id: UUID, data: dict) -> Optional[GroceryItem]:
        item = self.get(item_id)
        if item is None:
            return None
        updated = item.model_copy(update=data)
        index = self._items.index(item)
        self._items[index] = updated
        return updated

    def delete(self, item_id: UUID) -> bool:
        item = self.get(item_id)
        if item is None:
            return False
        self._items.remove(item)
        return True

