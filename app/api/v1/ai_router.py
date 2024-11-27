from fastapi import APIRouter, Depends
from app.schemas.ai import UserAIRequest
from app.services.ai_service import AIChatbotService

router = APIRouter()


def get_ai_chatbot_service():
    return AIChatbotService()


@router.post("/ai/chatbot")
async def ai_chatbot(
    request: UserAIRequest,
    ai_chatbot_service: AIChatbotService = Depends(get_ai_chatbot_service),
):
    return await ai_chatbot_service.process_chatbot_request(request)
