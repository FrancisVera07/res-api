# Manejo de datos/consultas

def indvidual_data(product):
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "category": product["category"],
        "imgURL": product["imgURL"],
        "created_at": product["created_at"],
        "updated_at": product["updated_at"]
    }

def all_data(products):
    return [indvidual_data(product) for product in products]