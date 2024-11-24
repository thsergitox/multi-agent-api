from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class LatexDocSchema(BaseModel):
    latex: str
    
class SearchSchema(BaseModel):
    query:str


## TODO: Agregar Schemas para el chatbot AI 