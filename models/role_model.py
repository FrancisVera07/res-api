from pydantic import BaseModel, validator
from datetime import datetime
from middlewares.role_middleware import validate_role

class Role(BaseModel):
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @validator("name")
    def validate_role(cls, v):
        return validate_role(cls, v)