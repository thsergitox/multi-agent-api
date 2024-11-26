from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import UserService
from app.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema
from dependency_injector.wiring import inject, Provide
from app.container import Container

router = APIRouter()

@router.get("/", response_model=list[UserSchema])
@inject
def list_users(
    user_service: UserService = Depends(Provide[Container.user_service])
):
    try:
        return user_service.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=UserSchema)
@inject
def create_user(
    user_data: UserCreateSchema,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    try:
        return user_service.create_user(user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{user_id}", response_model=UserSchema)
@inject
def update_user(
    user_id: str,
    user_data: UserUpdateSchema,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    try:
        return user_service.update_user(user_id, user_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_id}", response_model=bool)
@inject
def delete_user(
    user_id: str,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    try:
        return user_service.delete_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
