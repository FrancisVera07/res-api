# Proteccion de las rutas
import os
import jwt
from datetime import datetime
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

# Variables de entorno
load_dotenv(".env")
secret = os.getenv("SECRET")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def route_protect(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        # Validar expiracion
        if datetime.utcnow() > datetime.utcfromtimestamp(payload["exp"]):
            raise HTTPException(
                status_code=401,
                detail="El token ha expirado",
            )
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
