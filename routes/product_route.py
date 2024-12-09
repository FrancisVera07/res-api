from fastapi import APIRouter, Depends
from controllers.product_controller import get_all_products, get_product, create_product, update_product, delete_product
from models.product_model import Product
from helpers.protect_routes import route_protect

router = APIRouter(
    prefix="/api/product",
    tags=["Products"],)

# Ver productos
@router.get("/")
async def get_products():
    return await get_all_products()

# Ver prodyctos por id
@router.get("/{id}")
async def get_products_by_id(id: str):
    return await get_product(id)

# Agregar productos
@router.post("/")
async def post_products(new_product: Product, payload: dict = Depends(route_protect)):

    return await create_product(new_product)

# Actualizar productos
@router.put("/{id}")
async def put_products(id: str, updated_product: Product, payload: dict = Depends(route_protect)):

    return await update_product(id, updated_product)

# Eliminar productos
@router.delete("/{id}")
async def delete_products(id: str, payload: dict = Depends(route_protect)):
    return await delete_product(id)
