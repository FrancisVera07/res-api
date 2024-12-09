import re

def validate_username(cls, v):
    if not v or len(v.strip()) == 0:
        raise ValueError("El nombre del usuario no puede estar vacío.")
    if v.strip().lower() == "string":
        raise ValueError("El nombre del usuario no puede ser 'string'.")
    if len(v.strip()) < 5:
        raise ValueError("El nombre del usuario debe tener al menos 5 caracteres.")
    if len(v.strip()) > 25:
        raise ValueError("El nombre del usuario no puede tener más de 25 caracteres.")
    return v

def validate_password(cls, v):
    if not v or len(v.strip()) == 0:
        raise ValueError("La contraseña no puede estar vacío.")
    if v.strip().lower() == "string":
        raise ValueError("La contraseña no puede ser 'string'.")
    if len(v.strip()) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    if len(v.strip()) > 25:
        raise ValueError("La contraseña no puede tener más de 25 caracteres.")
    if not any(char.isupper() for char in v):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
    if not any(char.isdigit() for char in v):
        raise ValueError("La contraseña debe contener al menos un número.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
        raise ValueError("La contraseña debe contener al menos un carácter especial.")
    return v

def validate_email(cls, v):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not v or len(v.strip()) == 0:
        raise ValueError("El correo electrónico no puede estar vacío.")
    if not re.match(email_regex, v.strip()):
        raise ValueError("El correo electrónico no es válido.")
    return v

def validate_password_login(cls, v):
    if not v or len(v.strip()) == 0:
        raise ValueError("La contraseña no puede estar vacío.")
    return v