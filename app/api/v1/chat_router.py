from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from app.schemas.chat import ChatMessageSchema, ChatMessageCreateSchema
from app.services.chat_service import ChatService
from app.container import Container

router = APIRouter()

@router.get("/", response_model=list[ChatMessageSchema])
@inject
def list_chat_messages(chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.get_all_messages()

@router.get("/{message_id}", response_model=ChatMessageSchema)
def get_chat_message(message_id: str, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.get_message(message_id)

@router.post("/", response_model=ChatMessageSchema)
def create_chat_message(message_data: ChatMessageCreateSchema, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.create_message(message_data.dict())

@router.delete("/{message_id}")
def delete_chat_message(message_id: str, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.delete_message(message_id)