from uuid import uuid4
import pytest
from models.todo import TodoCreate
from repositories.in_memory_todo_repository import InMemoryTodoRepository
from services.todo_service import TodoService, TodoNotFoundError

def test_create_todo_returns_a_todo_with_the_given_title():
    service = TodoService(InMemoryTodoRepository())

    todo = service.create_todo(TodoCreate(title="Buy milk"))

    assert todo.title == "Buy milk"
    assert todo.completed is False
def test_get_todo_raises_when_it_does_not_exist():
    service = TodoService(InMemoryTodoRepository())
    with pytest.raises(TodoNotFoundError):
        service.get_todo(uuid4())
def test_delete_todo_removes_it_from_the_repository():
    service = TodoService(InMemoryTodoRepository())

    todo = service.create_todo(TodoCreate(title="Buy milk"))

    service.delete_todo(todo.id)
    with pytest.raises(TodoNotFoundError):
        service.get_todo(todo.id)