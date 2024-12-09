from datetime import datetime
from config.database import rolesCollections
from models.role_model import Role

def create_role(new_user):
    roles_to_add = []
    for role in new_user.roles:
        existing_role = rolesCollections.find_one({"name": role.name})

        # Si el rol no existe, lo creamos
        if not existing_role:
            # Crear el rol en la base de datos si no existe
            new_role = Role(name=role.name, created_at=datetime.now(), updated_at=datetime.now())
            role_dict = new_role.dict()
            role_dict['created_at'] = role_dict['created_at'].isoformat()
            role_dict['updated_at'] = role_dict['updated_at'].isoformat()

            rolesCollections.insert_one(role_dict)
            roles_to_add.append(role.name)
        else:
            roles_to_add.append(role.name)

    new_user.roles = roles_to_add