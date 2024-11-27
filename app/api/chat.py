from fastapi import APIRouter, Depends
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chatbot_service import ChatbotService
from app.container import Container

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chatbot_service: ChatbotService = Depends(lambda: Container.chatbot_service()),
) -> ChatResponse:
    return await chatbot_service.handle_message(request)
