from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.container import Container

container = Container()

db = container.db()
db.create_database()

# Creación de la aplicación FastAPI
app = FastAPI(
    title="Searcher API",
    description="API para autenticación de usuarios",
    version="0.1"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

# Inyección de dependencias
app.container = container

app.include_router(router, prefix="/api")
