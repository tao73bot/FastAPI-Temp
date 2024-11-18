from fastapi import APIRouter, HTTPException, Depends
from .models import UserCreate
from .repository import create_user, authenticate_user

router = APIRouter()

@router.post("/signup", response_model=str)
async def signup(user: UserCreate):
    db_user = await create_user(user)
    return db_user.username

@router.post("/login")
async def login(user: UserCreate):
    token = await authenticate_user(user.username, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
