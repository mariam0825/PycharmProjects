from datetime import datetime, timezone
from typing import List, Optional
from uuid import UUID
from pymongo import ReturnDocument
from pymongo.collection import Collection
from models.todo import Todo
from repositories.todo_repository import TodoRepository
class MongoTodoRepository(TodoRepository):

    """Same contract as InMemoryTodoRepository, backed by MongoDB."""

    def __init__(self, collection: Collection):
        self._collection = collection

    def add(self, todo: Todo) -> Todo:
        self._collection.insert_one(self._to_document(todo))
        return todo

    def get(self, todo_id: UUID) -> Optional[Todo]:
        document = self._collection.find_one({"_id": str(todo_id)})
        return self._to_entity(document) if document else None

    def list(self) -> List[Todo]:
        return [self._to_entity(doc) for doc in self._collection.find()]

    def update(self, todo_id: UUID, data: dict) -> Optional[Todo]:
        data["updated_at"] = datetime.now(timezone.utc)
        document = self._collection.find_one_and_update(
            {"_id": str(todo_id)},
            {"$set": data},
        return_document=ReturnDocument.AFTER,
        )
        return self._to_entity(document) if document else None
    def delete(self, todo_id: UUID) -> bool:
        result = self._collection.delete_one({"_id": str(todo_id)})
        return result.deleted_count == 1

    @staticmethod
    def _to_document(todo: Todo) -> dict:
        document = todo.model_dump()
        document["_id"] = str(document.pop("id"))
        return document

    @staticmethod
    def _to_entity(document: dict) -> Todo:
        document = dict(document)
        document["id"] = document.pop("_id")
        return Todo(**document)