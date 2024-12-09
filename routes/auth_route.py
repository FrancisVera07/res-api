from fastapi import APIRouter
from controllers.auth_controller import create_user, login_user
from models.user_model import User, UserLogin

router = APIRouter(
    prefix="/api/user",
    tags=["Users"],)

# Registrar usuario
@router.post("/register")
async def register_user(new_user: User):
    return await create_user(new_user)

# Iniciar sesion
@router.post("/login")
async def enter_user(user: UserLogin):
    return await login_user(user)