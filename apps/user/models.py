from pydantic import BaseModel
from bson import ObjectId

# Pydantic model for User input
class UserCreate(BaseModel):
    username: str
    password: str

# Pydantic model for User in DB (after hashing password)
class UserInDB(BaseModel):
    username: str
    hashed_password: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat data as a dict, not a class

# MongoDB User schema (includes _id)
class UserMongo(BaseModel):
    _id: ObjectId
    username: str
    full_name: str
    hashed_password: str

    class Config:
        arbitrary_types_allowed = True  # Allow ObjectId type from MongoDB
