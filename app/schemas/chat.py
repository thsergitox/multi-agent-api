from pydantic import BaseModel
from typing import Optional

class ChatMessageSchema(BaseModel):
    id: Optional[int]  # ID del mensaje, opcional para respuestas
    user_id: int  # Usuario que envió el mensaje
    project_id: int  # Proyecto asociado al mensaje
    content: str  # Contenido del mensaje

    class Config:
        from_attributes = True

class ChatMessageCreateSchema(BaseModel):
    user_id: int
    project_id: int
    content: str
