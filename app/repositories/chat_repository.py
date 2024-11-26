from sqlalchemy.orm import Session
from typing import Callable, List, Dict
from contextlib import AbstractContextManager
from uuid import UUID

from app.models.chat import ChatMessage
from app.repositories.interfaces.chat_repository_interface import ChatRepositoryInterface

class ChatRepository(ChatRepositoryInterface):
    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    # Obtener todos los mensajes de chat
    def get_all_chats(self) -> List[ChatMessage]:
        with self.db() as session:
            return session.query(ChatMessage).all()

    # Obtener un mensaje de chat por su ID
    def get_chat_by_id(self, chat_id: UUID) -> ChatMessage:
        with self.db() as session:
            return session.query(ChatMessage).filter(ChatMessage.id == chat_id).first()

    # Crear un nuevo mensaje de chat
    def create_chat(self, chat_data: Dict) -> ChatMessage:
        with self.db() as session:
            new_chat = ChatMessage(**chat_data)
            session.add(new_chat)
            session.commit()
            session.refresh(new_chat)
        return new_chat

    # Actualizar un mensaje existente
    def update_chat(self, chat_id: UUID, updates: Dict) -> ChatMessage:
        with self.db() as session:
            chat = session.query(ChatMessage).filter(ChatMessage.id == chat_id).first()
            if not chat:
                return None
            for key, value in updates.items():
                setattr(chat, key, value)
            session.commit()
            session.refresh(chat)
        return chat

    # Eliminar un mensaje de chat
    def delete_chat(self, chat_id: UUID) -> None:
        with self.db() as session:
            chat = session.query(ChatMessage).filter(ChatMessage.id == chat_id).first()
            if not chat:
                return
            session.delete(chat)
            session.commit()

    def get_by_user_in_project(self, user_id: str, project_id: str) -> List[ChatMessage]:
        with self.db() as session:
            return session.query(ChatMessage).filter(
                ChatMessage.user_id == user_id,
                ChatMessage.project_id == project_id
            ).all()
            