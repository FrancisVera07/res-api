def validate_name(cls, v):
    if not v or len(v.strip()) == 0:
        raise ValueError("El nombre del producto no puede estar vacío.")
    if v.strip().lower() == "string":
        raise ValueError("El nombre del producto no puede ser 'string'.")
    if len(v.strip()) < 5:
        raise ValueError("El nombre del producto debe tener al menos 5 caracteres.")
    if len(v.strip()) > 25:
        raise ValueError("El nombre del producto no puede tener más de 25 caracteres.")
    return v

def validate_price(cls, v):
    if not isinstance(v, (int, float)):
        raise ValueError("El precio debe ser un número.")
    if v < 0:
        raise ValueError("El precio no puede ser negativo.")
    if v == 0:
        raise ValueError("El precio no puede ser 0.")
    if v > 1000:
        raise ValueError("El precio no puede ser mayor a 1000.")
    if v < 10:
        raise ValueError("El precio no puede ser menor a 10.")
    return v

def validate_category(cls, v):
    if not v or len(v.strip()) == 0:
        raise ValueError("La categoria del producto no puede estar vacío.")
    if v.strip().lower() == "string":
        raise ValueError("La categoria del producto no puede ser 'string'.")
    return v

def validate_imgURL(cls, v):
    if not v or len(v.strip()) == 0:
        raise ValueError("La URL de la imagen del producto no puede estar vacía.")
    if v.strip().lower() == "string":
        raise ValueError("La URL de la imagen del producto no puede ser 'string'.")
    return v