import uuid
from typing import Optional
from app.schemas.chat import ChatRequest, ChatResponse


class ChatbotService:
    def __init__(self):
        # In a real implementation, you might want to inject a chat model or database here
        self.conversations = {}  # Simple in-memory storage for demo

    async def handle_message(self, chat_request: ChatRequest) -> ChatResponse:
        session_id = chat_request.sessionId or str(uuid.uuid4())

        # Store conversation history if needed
        if session_id not in self.conversations:
            self.conversations[session_id] = []
        self.conversations[session_id].append(chat_request.message)

        # Simple echo response for demonstration
        # In a real implementation, you would process the message here
        response = f"You said: {chat_request.message}"

        return ChatResponse(response=response, sessionId=session_id)
