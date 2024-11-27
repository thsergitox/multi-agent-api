from abc import ABC, abstractmethod
from app.schemas.ai import UserAIRequest


class AIChatbotServiceInterface(ABC):
    @abstractmethod
    async def process_chatbot_request(self, request: UserAIRequest):
        """Process an AI chatbot request and return the response"""
        pass
