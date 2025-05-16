from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(request: LoginRequest):
    # implementar logica despues, esto es para tener algo no mas
    return {"access_token": "mock-toen", "token_type": "bearer"}
