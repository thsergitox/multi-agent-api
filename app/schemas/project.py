from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class ProjectSchema(BaseModel):
    id: UUID  # ID del proyecto como UUID
    title: str  # Título del proyecto
    description: Optional[str] = None  # Descripción, puede estar vacío
    is_public: bool  # Si el proyecto es público o privado
    created_at: datetime  # Fecha de creación
    updated_at: datetime  # Fecha de última actualización

    class Config:
        from_attributes = True

class PaperSchema(BaseModel):
    title: str
    authors: List[str]
    year: int

class ProjectCreateSchema(BaseModel):
    access_token: str
    title: str
    description: Optional[str] = None
    is_public: bool = True
    papers: List[PaperSchema] = Field(default_factory=list)

    class Config:
        json_schema_extra = {
            "example": {
                "access_token": "ingresa token valido",
                "title": "Proyecto de ejemplo",
                "description": "Descripción del proyecto",
                "is_public": True,
                "papers": [
                    {
                        "title": "Paper 1",
                        "authors": ["Author 1", "Author 2"],
                        "year": 2023
                    }
                ]
            }
        }

class ProjectUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_public: Optional[bool] = None

class UserProjectsRequestSchema(BaseModel):
    access_token: str