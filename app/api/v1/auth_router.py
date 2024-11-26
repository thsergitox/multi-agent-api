from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import inject, Provide
from sqlalchemy.exc import IntegrityError

from app.container import Container
from app.schemas.user import UserCreateSchema, UserSchema, UserLoginSchema, TokenSchema
from app.services.auth_service import AuthService
from app.config import settings

router = APIRouter()

JWT_SECRET_KEY = settings.JWT_SECRET_KEY

@router.post("/register")
@inject
def register_user(user_data: UserCreateSchema, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    try:
        token = auth_service.register_user(user_data)
        return { "access_token": token }
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 

@router.post("/login")
@inject
def login_user(user: UserLoginSchema, auth_service: AuthService = Depends(Provide[Container.auth_service])):
    try:
        token = auth_service.authenticate_user(user)
        return { "access_token": token }
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
