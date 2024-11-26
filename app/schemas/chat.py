from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ChatMessageSchema(BaseModel):
    id: Optional[UUID]  # ID del mensaje, opcional para respuestas
    user_id: UUID  # Usuario que envió el mensaje
    project_id: UUID  # Proyecto asociado al mensaje
    content: str  # Contenido del mensaje

    class Config:
        from_attributes = True

class ChatMessageCreateSchema(BaseModel):
    user_id: UUID
    project_id: UUID
    content: str

class ChatRequestSchema(BaseModel):
    access_token: str
    project_id: UUID