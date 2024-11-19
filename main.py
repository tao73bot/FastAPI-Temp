from fastapi import FastAPI
from apps.user.route import router as auth_router
from apps.todo.route import router as todo_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(todo_router, prefix="/todos", tags=["ToDos"])