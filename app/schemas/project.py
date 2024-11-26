from pydantic import BaseModel
from typing import Optional

class ProjectSchema(BaseModel):
    id: Optional[int]  # ID del proyecto, opcional para respuestas
    title: str  # Título del proyecto
    description: Optional[str] = None  # Descripción, puede estar vacío
    is_public: bool  # Si el proyecto es público o privado
    created_at: Optional[str] = None  # Fecha de creación
    updated_at: Optional[str] = None  # Fecha de última actualización

    class Config:
        from_attributes = True

class ProjectCreateSchema(BaseModel):
    title: str
    description: Optional[str] = None
    is_public: bool = False  # Por defecto, el proyecto no es público

class ProjectUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None
