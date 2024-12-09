from bson import ObjectId
from fastapi import HTTPException
from config.database import productsCollections
from helpers.product_helper import validate_object_id, exist_product, check_duplicates_create, check_duplicates_update
from schemas.product_schema import all_data, indvidual_data
from datetime import datetime

# Ver los productos
async def get_all_products():
    try:
        data = productsCollections.find()
        return all_data(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los productos: {e}")

# Ver productos por id
async def get_product(id):
    try:
        id = ObjectId(id)
        data = productsCollections.find_one({"_id": ObjectId(id)})
        # Validaciones
        validate_object_id(id)
        exist_product(data)
        return indvidual_data(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el producto: {e}")

# Agregar productos
async def create_product(new_product):
    try:
        # Validaciones
        check_duplicates_create(new_product)
        # Guardar producto
        productsCollections.insert_one(dict(new_product))
        return { "status_code": 200, "message": "Producto creado correctamente" }
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el producto: {e}")
    except Exception as e:
        raise e

# Actualizar productos
async def update_product(id, updated_product):
    try:
        id = ObjectId(id)
        data = productsCollections.find_one({"_id": ObjectId(id)})
        # Validaciones
        validate_object_id(id)
        exist_product(data)
        check_duplicates_update(id, updated_product)
        # Modificar fecha de actualizacion
        updated_product_dict = updated_product.dict()
        updated_product_dict['updated_at'] = datetime.now()
        # Guardar producto
        productsCollections.update_one({"_id": ObjectId(id)}, {"$set":  updated_product_dict})
        return { "status_code": 200, "message": "Producto actualizado correctamente" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el producto: {e}")

# Eliminar productos
async def delete_product(id):
    try:
        id = ObjectId(id)
        data = productsCollections.find_one({"_id": ObjectId(id)})
        # Validaciones
        validate_object_id(id)
        exist_product(data)
        # Eliminar producto
        productsCollections.delete_one({"_id": ObjectId(id)})
        return { "status_code": 200, "message": "Producto eliminado correctamente" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el producto: {e}")