from fastapi import Depends
from database import grocery_items_collection
from repositories.grocery_list_repository import GroceryItemRepository
from repositories.mongo_grocery_list_repository import MongoGroceryItemRepository
from services.grocery_list_service import GroceryItemService
_repository = MongoGroceryItemRepository(grocery_items_collection)


def get_grocery_item_repository() -> GroceryItemRepository:
    return _repository


def get_grocery_item_service(
    repository: GroceryItemRepository = Depends(get_grocery_item_repository),
) -> GroceryItemService:
    return GroceryItemService(repository)
