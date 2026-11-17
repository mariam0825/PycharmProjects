from fastapi import FastAPI
from controllers.grocery_list_controller import router as grocery_item_router
app = FastAPI(title="Grocery List Manager API")

app.include_router(grocery_item_router)
