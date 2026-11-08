from typing import List
from uuid import UUID
from models.todo import Todo, TodoCreate, TodoUpdate
from repositories.todo_repository import TodoRepository

class TodoNotFoundError(Exception):
    """Raised when a todo does not exist. The Controller turns this
    into a proper HTTP 404 -- the Service knows nothing about HTTP."""
    pass
class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, payload: TodoCreate) -> Todo:
        todo = Todo(title=payload.title, description=payload.description)
        return self.repository.add(todo)

    def list_todos(self) -> List[Todo]:
        return self.repository.list()

    def get_todo(self, todo_id: UUID) -> Todo:
        todo = self.repository.get(todo_id)
        if todo is None:
            raise TodoNotFoundError(f"Todo {todo_id} not found")
        return todo
    def update_todo(self, todo_id: UUID, payload: TodoUpdate) -> Todo:
        data = payload.model_dump(exclude_unset=True)
        todo = self.repository.update(todo_id, data)
        if todo is None:
            raise TodoNotFoundError(f"Todo {todo_id} not found")
        return todo
    def delete_todo(self, todo_id: UUID) -> None:
        deleted = self.repository.delete(todo_id)
        if not deleted:
            raise TodoNotFoundError(f"Todo {todo_id} not found")