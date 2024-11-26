# app/repositories/interfaces/chat_repository_interface.py

from abc import ABC, abstractmethod
from typing import List, Dict

class ChatRepositoryInterface(ABC):
    @abstractmethod
    def get_all_chats(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_chat_by_id(self, chat_id: int) -> Dict:
        pass

    @abstractmethod
    def create_chat(self, chat_data: Dict) -> Dict:
        pass

    @abstractmethod
    def update_chat(self, chat_id: int, updates: Dict) -> Dict:
        pass

    @abstractmethod
    def delete_chat(self, chat_id: int) -> None:
        pass
