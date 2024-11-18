from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    # These fields are required and will be loaded from environment variables
    mongo_url: str = os.getenv("MONGO_URL")
    db_name: str = os.getenv("DB_NAME")
    jwt_secret_key: str = os.getenv("JWT_SECRET")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
    jwt_expiration_minutes: int =os.getenv("JWT_EXPIRY") # This needs to be parsed correctly if it's in "30m" or "1h" format

    # Optional fields with default values (if any)
    db_uri: Optional[str] = None

    # # Custom validator to handle "30m" or "1h" type values for `jwt_expiration_minutes`
    # @field_validator("jwt_expiration_minutes", mode="before")
    # def parse_jwt_expiration_minutes(cls, value):
    #     if isinstance(value, str):
    #         # Handle '30m' or '1h' style inputs
    #         if value.endswith("m"):
    #             return int(value[:-1])  # Strip 'm' and convert to integer
    #         elif value.endswith("h"):
    #             return int(value[:-1]) * 60  # Convert hours to minutes
    #     return value  # Return the value as-is if it's already an integer

    # class Config:
    #     env_file = ".env"  # Specifies the .env file to load

# Initialize settings
settings = Settings()

# Create a MongoDB client
client = AsyncIOMotorClient(settings.mongo_url)
db = client[settings.db_name]  # Use the configured database
