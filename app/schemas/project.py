from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class ProjectSchema(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    is_public: bool
    created_at: datetime
    updated_at: datetime
    papers: List[dict]

    class Config:
        from_attributes = True

class PaperSchema(BaseModel):
    title: str
    abstract: str
    authors: List[str]
    categories: str
    entry_id: str
    pdf_url: str
    published: str
    updated: str

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
                        "title": "Quantum Cryptography for Enhanced Network Security: A Comprehensive Survey",
                        "abstract": "With the ever-growing concern for internet security, the field of quantum cryptography emerges as a promising solution...",
                        "authors": ["Mst Shapna Akter"],
                        "categories": "cs.CR",
                        "entry_id": "http://arxiv.org/abs/2306.09248v1",
                        "pdf_url": "http://arxiv.org/pdf/2306.09248v1",
                        "published": "2023-06-02",
                        "updated": "2023-06-02"
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