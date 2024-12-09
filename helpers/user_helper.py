import os
import jwt
import hashlib
import datetime
from dotenv import load_dotenv
from fastapi import HTTPException
from config.database import usersCollections

# Variables de entorno
load_dotenv(".env")
secret = os.getenv("SECRET")

# Encriptacion de contraseña
def encrypt_pass(password):
    # Pasar contraseña a bytes
    pass_byte = password.encode("utf-8")
    hashed_pass = hashlib.sha256(pass_byte).hexdigest()
    return hashed_pass

# Validar duplicados al crear
def check_duplicates_create(new_user):
    existing_username = usersCollections.find_one({
        "username": new_user.username,
    })
    existing_email = usersCollections.find_one({
        "email": new_user.email
    })
    if existing_username:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    if existing_email:
        raise HTTPException(status_code=400, detail="El correo ya existe")

# Validar existencia de datos
def check_login(login_user):
    # Encriptar la contraseña
    pass_encrypt = encrypt_pass(login_user.password)
    existing_email = usersCollections.find_one({
        "email": login_user.email,
    })
    existing_user = usersCollections.find_one({
        "email": login_user.email,
        "password": pass_encrypt
    })
    if not existing_email:
        raise HTTPException(status_code=400, detail="No se encontró el correo")
    if not existing_user:
        raise HTTPException(status_code=400, detail="No se encontró el usuario")
    return existing_user

# Generar un JWT
def create_jwt(payload, algorithm="HS256", expiration=1):
    payload = payload.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration)
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

