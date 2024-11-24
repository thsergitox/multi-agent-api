from fastapi import APIRouter
from app.api.v1.auth_router import router as api_router

router = APIRouter()

router.include_router(api_router, prefix="/auth", tags=["auth"])