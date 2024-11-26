from app.repositories.chat_repository import ChatRepository
from app.models.chat import ChatMessage
from uuid import UUID
from app.services.interfaces.token_service_interface import TokenServiceInterface

class ChatService:
    def __init__(self, chat_repository: ChatRepository, token_service: TokenServiceInterface):
        self.chat_repository = chat_repository
        self.token_service = token_service

    def get_message(self, message_id: UUID):
        message = self.chat_repository.get_chat_by_id(message_id)
        if not message:
            raise ValueError(f"Chat message with ID {message_id} not found")
        return message

    def create_message(self, message_data: dict):
        return self.chat_repository.create_chat(message_data)

    def update_message(self, message_id: UUID, updates: dict):
        message = self.chat_repository.update_chat(message_id, updates)
        if not message:
            raise ValueError(f"Chat message with ID {message_id} not found")
        return message

    def delete_message(self, message_id: UUID):
        success = self.chat_repository.delete_chat(message_id)
        if not success:
            raise ValueError(f"Chat message with ID {message_id} not found")
        return success

    def get_all_messages(self):
        return self.chat_repository.get_all_chats()

    def get_chats_by_project_and_user(self, access_token: str, project_id: UUID):
        token_data = self.token_service.verify_token(access_token)
        if not token_data or 'sub' not in token_data:
            raise ValueError("Invalid token")
        
        user_id = token_data['sub']
        return self.chat_repository.get_by_user_in_project(user_id, project_id)