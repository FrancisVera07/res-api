from fastapi import FastAPI
from routes import product_route, auth_route
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitr CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(product_route.router)
app.include_router(auth_route.router)
