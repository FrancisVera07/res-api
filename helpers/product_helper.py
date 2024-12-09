from bson import ObjectId
from fastapi import HTTPException
from config.database import productsCollections

def validate_object_id(id):
    if not ObjectId.is_valid:
        raise HTTPException(status_code=400, detail="ID inválido")

def exist_product(data: dict):
    if not data:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

# Validar duplicados al crear
def check_duplicates_create(new_product):
    existing_product = productsCollections.find_one({
        "name": new_product.name,
        "category": new_product.category,
    })

    if existing_product:
        raise HTTPException(status_code=400, detail="El producto ya existe")

# Validar duplicados en actualizacion
def check_duplicates_update(id, updated_product):
    id = ObjectId(id)
    existing_product = productsCollections.find_one({
        "name": updated_product.name,
        "category": updated_product.category,
    })

    if existing_product and existing_product["_id"] != id:
        raise HTTPException(status_code=400, detail="El producto ya existe")