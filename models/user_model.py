from typing import List
from datetime import datetime
from pydantic import BaseModel, validator
from middlewares.user_middleware import validate_username, validate_password, validate_email, validate_password_login
from models.role_model import Role

class User(BaseModel):
    username: str
    password: str
    email: str
    roles: List[Role]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @validator("username")
    def validate_username(cls, v):
        return validate_username(cls, v)

    @validator("password")
    def validate_password(cls, v):
        return validate_password(cls, v)

    @validator("email")
    def validate_email(cls, v):
        return validate_email(cls, v)

class UserLogin(BaseModel):
    email: str
    password: str

    @validator("password")
    def validate_password(cls, v):
        return validate_password_login(cls, v)

    @validator("email")
    def validate_email(cls, v):
        return validate_email(cls, v)