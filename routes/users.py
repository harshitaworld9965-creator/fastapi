from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    name: str
    age: int
    city: str

@router.post("/users")
def create_user(user: User):
    return {"message": "User created!", "user": user}
