from uuid import uuid4
import pytest
from fastapi.testclient import TestClient
from main import app
from dependencies import get_todo_repository
from repositories.in_memory_todo_repository import InMemoryTodoRepository

@pytest.fixture
def client():
    repository = InMemoryTodoRepository()
    app.dependency_overrides[get_todo_repository] = lambda: repository
    yield TestClient(app)
    app.dependency_overrides.clear()

def test_create_todo_returns_201_and_the_created_todo(client):
    response = client.post("/todos/", json={"title": "Buy milk"})

    assert response.status_code == 201
    assert response.json()["title"] == "Buy milk"

def test_get_missing_todo_returns_404(client):
    response = client.get(f"/todos/{uuid4()}")
    assert response.status_code == 404

def test_full_crud_flow(client):
    create = client.post("/todos/", json={"title": "Walk the dog"})

    todo_id = create.json()["id"]
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 200

    patch_response = client.patch(f"/todos/{todo_id}", json={"completed": True})
    assert patch_response.json()["completed"] is True

    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 204