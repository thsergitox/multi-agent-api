from pydantic import BaseModel
from typing import Dict, List


class Message(BaseModel):
    content: str
    role: str

class Paper(BaseModel):
    title: str
    authors: List[str]
    abstract: str
    published: str
    updated: str
    pdf_url: str
    entry_id: str
    categories: str

class UserAIRequest(BaseModel):
    messages: List[Message]
    papers: List[Paper]

    class Config:
        json_schema_extra = {
            "example": {
                "messages": [
                    {
                        "content": "Hola, soy un estudiante de doctorado en el campo de la criptografía cuántica y estoy escribiendo un artículo científico sobre el estado actual de la investigación en este campo. Me gustaría recibir sugerencias sobre cómo mejorar la sección de introducción de mi artículo, que actualmente describe los conceptos básicos de la criptografía cuántica y su importancia para la seguridad de la información. Además, me gustaría que me ayudes a identificar las tendencias y desafíos actuales en la investigación en criptografía cuántica, y a sugerir referencias relevantes que pueda citar en mi trabajo. ¿Puedes ayudarme con esto?",
                        "role": "user"
                    }
                ]
            }
                }
                