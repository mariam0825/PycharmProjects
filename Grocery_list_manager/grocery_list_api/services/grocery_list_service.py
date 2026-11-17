from typing import List
from uuid import UUID

from models.grocery_list import GroceryItem, GroceryItemCreate
from repositories.grocery_list_repository import GroceryItemRepository

class GroceryItemNotFoundError(Exception):
    """Raise an Exception, when a grocery item does not exist."""
    pass

class GroceryItemService:
    def __init__(self, repository: GroceryItemRepository):
        self.repository = repository

    def create_grocery_item(self, payload: GroceryItemCreate) -> GroceryItem:
        item = GroceryItem(name=payload.name,quantity=payload.quantity)
        return self.repository.add(item)

    def list_grocery_items(self) -> List[GroceryItem]:
        return self.repository.list()

    def get_grocery_item(self, item_id: UUID) -> GroceryItem:
        item = self.repository.get(item_id)
        if item is None:
            raise GroceryItemNotFoundError(f"Grocery item {item_id} not found")

        return item

    def update_grocery_item(self, item_id: UUID, payload: GroceryItemUpdate) -> GroceryItem:
        data = payload.model_dump(exclude_unset=True)
        item = self.repository.update(item_id, data)
        if item is None:
            raise GroceryItemNotFoundError(
                f"Grocery item {item_id} not found")

        return item

    def delete_grocery_item(self, item_id: UUID) -> None:
        deleted = self.repository.delete(item_id)
        if not deleted:
            raise GroceryItemNotFoundError(f"Grocery item {item_id} not found")
