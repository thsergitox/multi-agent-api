from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

# Esquema para representar un usuario
class UserSchema(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True

# Esquema para crear un usuario
class UserCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str

# Esquema para inicio de sesión
class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

# Esquema para actualizar un usuario
class UserUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        from_attributes = True

# Esquema para documentos LaTeX
class LatexDocSchema(BaseModel):
    latex: str

# Esquema para búsquedas
class SearchSchema(BaseModel):
    query: str

# Esquema para el chatbot AI
class ChatMessageSchema(BaseModel):
    id: Optional[int]
    user_id: int
    project_id: int
    content: str

    class Config:
        from_attributes = True

class ChatMessageCreateSchema(BaseModel):
    user_id: int
    project_id: int
    content: str
