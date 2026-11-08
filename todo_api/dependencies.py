from fastapi import Depends
from database import todos_collection
from repositories.todo_repository import TodoRepository
from repositories.mongo_todo_repository import MongoTodoRepository
from services.todo_service import TodoService

_repository = MongoTodoRepository(todos_collection)
# was: _repository = InMemoryTodoRepository()

def get_todo_repository() -> TodoRepository:
    return _repository
def get_todo_service(
    repository: TodoRepository = Depends(get_todo_repository),
) -> TodoService:
    return TodoService(repository)