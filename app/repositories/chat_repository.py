from sqlalchemy.orm import Session
from typing import Callable, List
from contextlib import AbstractContextManager

from app.models.chat import ChatMessage
from app.repositories.interfaces.chat_repository_interface import ChatRepositoryInterface

class ChatRepository(ChatRepositoryInterface):
    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    # Obtener un mensaje de chat por su ID
    def get_by_id(self, message_id: str) -> ChatMessage:
        with self.db() as session:
            return session.query(ChatMessage).filter(ChatMessage.id == message_id).first()

    # Obtener todos los mensajes de un proyecto
    def get_by_project_id(self, project_id: str) -> List[ChatMessage]:
        with self.db() as session:
            return session.query(ChatMessage).filter(ChatMessage.project_id == project_id).all()

    # Obtener todos los mensajes de un usuario en un proyecto
    def get_by_user_in_project(self, user_id: str, project_id: str) -> List[ChatMessage]:
        with self.db() as session:
            return session.query(ChatMessage).filter(
                ChatMessage.user_id == user_id,
                ChatMessage.project_id == project_id
            ).all()

    # Crear un nuevo mensaje de chat
    def create_message(self, chat_message: ChatMessage) -> ChatMessage:
        with self.db() as session:
            session.add(chat_message)
            session.commit()
            session.refresh(chat_message)
        return chat_message

    # Actualizar un mensaje existente
    def update_message(self, message_id: str, updates: dict) -> ChatMessage:
        with self.db() as session:
            message = session.query(ChatMessage).filter(ChatMessage.id == message_id).first()
            if not message:
                return None  # Manejar de forma adecuada en la capa de servicio
            for key, value in updates.items():
                setattr(message, key, value)
            session.commit()
            session.refresh(message)
        return message

    # Eliminar un mensaje de chat
    def delete_message(self, message_id: str) -> bool:
        with self.db() as session:
            message = session.query(ChatMessage).filter(ChatMessage.id == message_id).first()
            if not message:
                return False  # Manejar de forma adecuada en la capa de servicio
            session.delete(message)
            session.commit()
        return True
