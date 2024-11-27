import uuid
from typing import Optional
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from app.schemas.chat import ChatRequest, ChatResponse
from app.config import settings


class ChatbotService:
    def __init__(self):
        # Initialize the language model
        self.llm = ChatOpenAI(
            temperature=0.7,
            model_name="gpt-3.5-turbo",
            openai_api_key=settings.OPENAI_API_KEY,
        )
        # Store conversation chains for each session
        self.conversations = {}

    def _get_or_create_conversation(self, session_id: str) -> ConversationChain:
        if session_id not in self.conversations:
            # Create a new conversation chain with memory
            memory = ConversationBufferMemory()
            self.conversations[session_id] = ConversationChain(
                llm=self.llm, memory=memory, verbose=True
            )
        return self.conversations[session_id]

    async def handle_message(self, chat_request: ChatRequest) -> ChatResponse:
        # Generate or use existing session ID
        session_id = chat_request.sessionId or str(uuid.uuid4())

        # Get or create conversation chain for this session
        conversation = self._get_or_create_conversation(session_id)

        # Process the message through the conversation chain
        response = conversation.predict(input=chat_request.message)

        return ChatResponse(response=response, sessionId=session_id)
