from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Variables de entorno
load_dotenv(".env")

uri = os.getenv("DATA_BASE")
client = MongoClient(uri, server_api=ServerApi("1"))
# Nombre de la base de datos
db = client.resApi
# Coleccion de productos
productsCollections = db["products"]
# Coleccion de usuarios
usersCollections = db["users"]
# Coleccion de roles
rolesCollections = db["roles"]