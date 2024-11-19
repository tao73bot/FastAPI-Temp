from .models import TodoCreate, TodoInDB, TodoUpdate, TodoDelete, TodoMongo
from config import db
from bson import ObjectId
from datetime import datetime

# Access the 'todos' collection from the db
todos_collection = db.todos

def todo_dict(todo: TodoMongo) -> dict:
    return {
        "id": str(todo["_id"]),
        "creator": str(todo["creator"]),
        "title": todo["title"],
        "description": todo["description"]
    }

async def get_todos_by_creator(creator: ObjectId) -> list:
    todos = []
    async for todo in todos_collection.find({"creator": creator}):
        todos.append(todo_dict(todo))
    return todos

async def get_todo_by_id(todo_id: ObjectId) -> TodoInDB:
    todo = await todos_collection.find_one({"_id": ObjectId(todo_id)})
    if todo:
        return TodoInDB(title=todo["title"], description=todo["description"])
    return None

async def create_todo(todo: TodoCreate, creator: ObjectId) -> TodoInDB:
    new_todo = {
        "creator": creator,
        "title": todo.title,
        "description": todo.description,
        "created_at": datetime.utcnow()
    }
    await todos_collection.insert_one(new_todo)
    return TodoInDB(title=todo.title, description=todo.description)

async def update_todo(todo_id: ObjectId, todo: TodoUpdate) -> TodoInDB:
    updated_todo = {
        "title": todo.title,
        "description": todo.description
    }
    await todos_collection.find_one_and_update({"_id": ObjectId(todo_id)}, {"$set": dict(updated_todo)})
    return TodoInDB(title=todo.title, description=todo.description)

async def delete_todo(todo_id: ObjectId) -> TodoDelete:
    await todos_collection.find_one_and_delete({"_id": ObjectId(todo_id)})
    return TodoDelete(title="Deleted")

async def delete_all_todos(creator: ObjectId) -> TodoDelete:
    await todos_collection.delete_many({"creator": creator})
    return TodoDelete(title="Deleted all todos")


