from pydantic import BaseModel, validator
from datetime import datetime
from middlewares.product_middleware import validate_name, validate_price, validate_category, validate_imgURL


class Product(BaseModel):
    name: str
    price: float
    category: str
    imgURL: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @validator("name")
    def validate_name(cls, v):
        return validate_name(cls, v)

    @validator("price")
    def validate_price(cls, v):
        return validate_price(cls, v)

    @validator("category")
    def validate_category(cls, v):
        return validate_category(cls, v)

    @validator("imgURL")
    def validate_imgURL(cls, v):
        return validate_imgURL(cls, v)