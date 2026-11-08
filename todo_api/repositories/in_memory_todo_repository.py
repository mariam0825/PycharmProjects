from typing import List, Optional
from uuid import UUID
from models.todo import Todo
from repositories.todo_repository import TodoRepository

class InMemoryTodoRepository(TodoRepository):
    """Stores todos in a plain Python list. No database needed yet."""
    def __init__(self):
        self._todos: List[Todo] = []

    def add(self, todo: Todo) -> Todo:
        self._todos.append(todo)
        return todo

    def get(self, todo_id: UUID) -> Optional[Todo]:
        for todo in self._todos:
            if todo.id == todo_id:
             return todo

    def list(self) -> List[Todo]:
        return self._todos

    def update(self, todo_id: UUID, data: dict) -> Optional[Todo]:
        todo = self.get(todo_id)
        if todo is None:
            return None
        updated = todo.model_copy(update=data)
        index = self._todos.index(todo)
        self._todos[index] = updated
        return updated

    def delete(self, todo_id: UUID) -> bool:
        todo = self.get(todo_id)
        if todo is None:
            return False
        self._todos.remove(todo)
        return True