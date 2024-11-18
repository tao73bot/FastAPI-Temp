from passlib.hash import bcrypt
from .models import UserCreate, UserInDB
from .services.auth_service import create_access_token
from config import db  # Import the db object
from datetime import datetime

# Access the 'users' collection from the db
users_collection = db.users  

# Function to hash a password using bcrypt
def hash_password(password: str) -> str:
    return bcrypt.hash(password)

# Function to verify a password using bcrypt
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.verify(plain_password, hashed_password)

async def get_user_by_username(username: str) -> UserInDB:
    user = await users_collection.find_one({"username": username})
    if user:
        return UserInDB(username=user["username"], hashed_password=user["hashed_password"])
    return None

async def create_user(user: UserCreate) -> UserInDB:
    # Hash the password
    hashed_password = hash_password(user.password)
    
    # Create a new user
    new_user = {
        "username": user.username,
        "hashed_password": hashed_password,
        "created_at": datetime.utcnow()
    }
    
    # Insert the new user into the 'users' collection
    result = await users_collection.insert_one(new_user)
    
    # Return the newly created user
    return UserInDB(username=user.username, hashed_password=hashed_password)

async def authenticate_user(username: str, password: str) -> str:
    # Get the user from the database
    user = await get_user_by_username(username)
    
    # Verify the password
    if not user or not verify_password(password, user.hashed_password):
        return None
    
    # Create an access token
    access_token = create_access_token(data={"sub": user.username})
    return access_token
