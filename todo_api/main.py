from fastapi import FastAPI
from controllers.todo_controller import router as todo_router

app = FastAPI(title="Todo API")

app.include_router(todo_router)