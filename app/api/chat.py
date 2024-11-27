from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chatbot_service import ChatbotService
from app.container import Container
import logging

# Configure logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/v1/ai/chatbot", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chatbot_service: ChatbotService = Depends(lambda: Container.chatbot_service()),
) -> ChatResponse:
    try:
        logger.info(f"Received chat request with message: {request.message[:50]}...")
        response = await chatbot_service.handle_message(request)
        logger.info(f"Successfully processed chat request")
        return response
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
