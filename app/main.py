from fastapi import FastAPI
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

# Inyección de dependencias
app.container = container

app.include_router(router, prefix="/api")
