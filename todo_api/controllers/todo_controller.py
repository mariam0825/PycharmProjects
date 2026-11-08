from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID
from models.todo import Todo, TodoCreate, TodoUpdate
from services.todo_service import TodoService, TodoNotFoundError
from dependencies import get_todo_service
router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(
    payload: TodoCreate,
     service: TodoService = Depends(get_todo_service),
):
    return service.create_todo(payload)

@router.get("/", response_model=list[Todo])
def list_todos(service: TodoService = Depends(get_todo_service)):
    return service.list_todos()

@router.get("/{todo_id}", response_model=Todo)
def get_todo(
    todo_id: UUID,
    service: TodoService = Depends(get_todo_service),
    ):
    try:
        return service.get_todo(todo_id)
    except TodoNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: UUID,
    payload: TodoUpdate,
    service: TodoService = Depends(get_todo_service),
    ):
    try:
        return service.update_todo(todo_id, payload)
    except TodoNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: UUID,
    service: TodoService = Depends(get_todo_service),
):
    try:
        service.delete_todo(todo_id)
    except TodoNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))