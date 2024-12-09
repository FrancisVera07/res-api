from fastapi import HTTPException
from config.database import usersCollections
from helpers.role_helper import create_role
from helpers.user_helper import encrypt_pass, check_duplicates_create, check_login, create_jwt


# Crear cuenta
async def create_user(new_user):
    try:
        # Crear/Asignar un rol
        create_role(new_user)
        # Validaciones
        check_duplicates_create(new_user)
        # Encriptar la contraseña
        pass_encrypt = encrypt_pass(new_user.password)
        user_dict = new_user.dict()
        # Guardar datos
        user_dict["password"] = pass_encrypt
        usersCollections.insert_one(user_dict)
        return { "status_code": 200, "message": "Usuario creado correctamente" }
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {e}")
    except Exception as e:
        raise e

# iniciar sesion
async def login_user(login_user):
    try:
        # Validaciones
        user = check_login(login_user)
        # Generar token
        payload = {
            "_id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]
        }
        token = create_jwt(payload)
        return { "status_code": 200, "message": token }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al iniciar sesion: {e}")

# eliminar cuenta
async def delete_user(id):
    try:
        return { "status_code": 200, "message": "Usuario eliminado correctamente" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {e}")

