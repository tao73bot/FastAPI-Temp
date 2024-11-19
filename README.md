# FAST API CRUD with MongoDB

## I follow this folder structure

```paintext
project/
│
├── .venv/                   # Virtual environment
│
├── apps/                     # Application-specific modules
│   ├── user/                 # User-related module
│   │   ├── models.py         # MongoDB models (e.g., User model)
│   │   ├── repository.py     # Data access logic (CRUD operations)
│   │   ├── route.py          # Routes for user-related endpoints
│   │   ├── schema.py         # Pydantic schemas for User validation
│   │   └── services/         # Services directory (business logic)
│   │       └── auth_service.py # Authentication logic
│   │
│   └── todo/                 # Todo-related module
│       ├── models.py         # MongoDB models (e.g., Todo model)
│       ├── repository.py     # Data access logic (CRUD operations)
│       ├── route.py          # Routes for todo-related endpoints
│       └── schema.py         # Pydantic schemas for Todo validation
│
├── config.py                 # Configuration settings for the project
├── main.py                   # FastAPI application entry point
├── requirements.txt          # List of project dependencies
├── .env                      # Environment variables (should not be in version control)
├── .gitignore                # Git ignore file to exclude unwanted files/folders
└── README.md                 # Project documentation

```

## Table of Contents

1. [Installation](#installation)  
2. [Running the Project](#running-the-project)  
3. [API Endpoints](#api-endpoints)  
   - [User Endpoints](#user-endpoints)  
   - [Task Endpoints](#task-endpoints)  
4. [Authentication](#authentication)  
5. [Environment Variables](#environment-variables)  
6. [Database](#database)  
7. [Testing](#testing)  
8. [Contributing](#contributing)  
9. [License](#license)

## Installation

### Prerequisites

Ensure the following are installed on your system:

- Python 3.6 or higher
- MongoDB (it can be cloud also)

### Steps

1. **Clone the repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. **Create and Activate virtual enviroment**  
    To do that run the following command
   ```bash
   # Create virtual enviroment
   python -m venv .venv
   # Acticate virtual enviroment
   source .venv/bin/activate # on mac and linux
   venv\Scripts\activate # on windows
   ```

3. **Install dependencies**  
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

Once the installation is complete, follow these steps to run the FastAPI application:

1. **Start the server**  
   Use `uvicorn` to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

- The `--reload` flag enables automatic code reload during development.


2. **Access the application**  
    By default, access point is:
    - **Base URL** `127.0.0.1:8000`

3. **Explore Api documentations**  
    Fast api provides interactive API documentation at these endpoints:
    - **Swagger UI** : http://127.0.0.1:8000/docs
    - **Redoc UI** : http://127.0.0.1:8000/redoc

### Run on different port
Use the `--port` flag to run the server on a custom port:
```bash
uvicorn main:app --reload --port 8080
```

## API Endpoints
### User Endpoints

`POST /auth/signup`
- **Description**: Create a new user.
- **Parameters**: None
- **Request body**:
```json
{
    "username": "string",
    "password": "string"
}
```
- **Response**:
```json
{
    "username": 
}
```

`POST /auth/login`
- **Description**: Login as user.
- **Parameters**: None
- **Request body**:
```json
{
    "username": "string",
    "password": "string"
}
```
- **Response**:
```json
{
    "username": 
}
```

### Task Endpoints




## Authentication

- **Mechanism**: Bearer Token (JWT)
- **Endpoints**:
    - `POST /auth/login` to get token
    - Use the token in the `Authorization` header:
    ```
    Authorization: Bearer <your_token>
    ```

## Environment Variables
Create a `.env` file in the root directory with the following keys:
```.env
MONGO_URL="mongodb://localhost:27017/"
DB_NAME="db_name"

# JWT Configuration
JWT_SECRET="mysecrect"
JWT_ALGORITHM="Algorithm"
JWT_EXPIRY=30  # Can be "30m", "1h", "15m", etc.

```

- **Config the settings using `.env` file**

## Database
- **Database Type**: MongoDB
- **Driver**: `motor`
- **Setup**: Use database `URI` from `.env` file
