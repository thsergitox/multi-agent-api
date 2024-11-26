from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import Provide, inject
from app.schemas.chat import ChatMessageSchema, ChatMessageCreateSchema, ChatRequestSchema 
from app.services.chat_service import ChatService
from app.container import Container
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[ChatMessageSchema])
@inject
def list_chat_messages(chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.get_all_messages()

@router.get("/{message_id}", response_model=ChatMessageSchema)
@inject
def get_chat_message(message_id: UUID, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.get_message(message_id)

@router.post("/", response_model=ChatMessageSchema)
@inject
def create_chat_message(message_data: ChatMessageCreateSchema, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.create_message(message_data.dict())

@router.delete("/{message_id}")
@inject
def delete_chat_message(message_id: UUID, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    return chat_service.delete_message(message_id)

@router.post("/get_byprojectanduser", response_model=list[ChatMessageSchema])
@inject
def get_chats_by_project_and_user(request: ChatRequestSchema, chat_service: ChatService = Depends(Provide[Container.chat_service])):
    try:
        return chat_service.get_chats_by_project_and_user(request.access_token, request.project_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
