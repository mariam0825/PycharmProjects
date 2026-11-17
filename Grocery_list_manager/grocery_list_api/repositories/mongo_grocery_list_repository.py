from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from pymongo import ReturnDocument
from pymongo.collection import Collection
from models.grocery_list import GroceryItem
from repositories.grocery_list_repository import GroceryItemRepository

class MongoGroceryItemRepository(GroceryItemRepository):

    def __init__(self, collection: Collection):
        self._collection = collection

    def add(self, item: GroceryItem) -> GroceryItem:
        self._collection.insert_one(self._to_document(item))
        return item

    def get(self, item_id: UUID) -> Optional[GroceryItem]:
        document = self._collection.find_one({"_id": str(item_id)})
        return self._to_entity(document) if document else None

    def list(self) -> List[GroceryItem]:
        return [self._to_entity(document)
            for document in self._collection.find()
        ]
    def update(
        self, item_id: UUID, data: dict
    ) -> Optional[GroceryItem]:
        data["updated_at"] = datetime.now(timezone.utc)
        document = self._collection.find_one_and_update(
            {"_id": str(item_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
        )
        return self._to_entity(document) if document else None

    def delete(self, item_id: UUID) -> bool:
        result = self._collection.delete_one(
            {"_id": str(item_id)}
        )
        return result.deleted_count == 1

    @staticmethod
    def _to_document(item: GroceryItem) -> dict:
        document = item.model_dump()
        document["_id"] = str(document.pop("id"))
        return document

    @staticmethod
    def _to_entity(document: dict) -> GroceryItem:
        document = dict(document)
        document["id"] = document.pop("_id")
        return GroceryItem(**document)

