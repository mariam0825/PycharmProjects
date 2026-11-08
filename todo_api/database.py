import os
from pymongo import MongoClient
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
database = client["todo_app"]
todos_collection = database["todos"]