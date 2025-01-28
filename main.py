from fastapi import FastAPI, HTTPException

app = FastAPI()

# Mock user data
users = [
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 22, "email": "charlie@example.com"}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/user/{id}")
def read_user(id: int):
    user = next((user for user in users if user["id"] == id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": id, "info": user}

