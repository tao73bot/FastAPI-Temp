from fastapi import APIRouter, HTTPException, Depends
from .models import TodoCreate, TodoInDB, TodoUpdate, TodoDelete
from .repository import get_todos_by_creator, get_todo_by_id, create_todo, update_todo, delete_todo, delete_all_todos
from apps.user.services.o_auth2 import get_current_user
from bson import ObjectId

router = APIRouter()

@router.get("/", response_model=list[TodoInDB])
async def read_todos(creator: str = Depends(get_current_user)):
    return await get_todos_by_creator(creator)

@router.get("/{todo_id}", response_model=TodoInDB)
async def read_todo(todo_id: str):
    return await get_todo_by_id(todo_id)

@router.post("/", response_model=TodoInDB)
async def create_todos(todo: TodoCreate, creator: str = Depends(get_current_user)):
    return await create_todo(todo, creator)

@router.put("/{todo_id}", response_model=TodoInDB)
async def update_todos(todo_id: str, todo: TodoUpdate, creator: str = Depends(get_current_user)):
    return await update_todo(todo_id, todo)

@router.delete("/{todo_id}", response_model=TodoDelete)
async def delete_todos(todo_id: str, creator: str = Depends(get_current_user)):
    return await delete_todo(todo_id)

@router.delete("/", response_model=TodoDelete)
async def delete_all_todos(creator: str = Depends(get_current_user)):
    return await delete_all_todos(creator)
