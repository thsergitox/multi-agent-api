from app.repositories.chat_repository import ChatRepository
from app.models.chat import ChatMessage

class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def get_message(self, message_id: str):
        message = self.chat_repository.get_by_id(message_id)
        if not message:
            raise ValueError(f"Chat message with ID {message_id} not found")
        return message

    def get_messages_by_project(self, project_id: str):
        return self.chat_repository.get_by_project_id(project_id)

    def create_message(self, message_data: dict):
        new_message = ChatMessage(**message_data)
        return self.chat_repository.create_message(new_message)

    def update_message(self, message_id: str, updates: dict):
        message = self.chat_repository.update_message(message_id, updates)
        if not message:
            raise ValueError(f"Chat message with ID {message_id} not found")
        return message

    def delete_message(self, message_id: str):
        success = self.chat_repository.delete_message(message_id)
        if not success:
            raise ValueError(f"Chat message with ID {message_id} not found")
        return success
