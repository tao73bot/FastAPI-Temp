from pydantic import BaseModel
from bson import ObjectId

# Pydantic model for Todo input
class TodoCreate(BaseModel):
    title: str
    description: str

# Pydantic model for Todo in DB
class TodoInDB(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat data as a dict

# MongoDB Todo schema (includes _id)
class TodoMongo(BaseModel):
    _id: ObjectId
    creator: ObjectId
    title: str
    description: str

    class Config:
        arbitrary_types_allowed = True  # Allow ObjectId type from MongoDB
