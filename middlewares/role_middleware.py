def validate_role(cls, v):
    allowed_roles = ["administrador", "cliente"]
    if not v or len(v.strip()) == 0:
        raise ValueError("El rol no puede estar vacío.")
    if v not in allowed_roles:
        raise ValueError(f"El rol debe ser uno de los siguientes: {', '.join(allowed_roles)}.")
    return v