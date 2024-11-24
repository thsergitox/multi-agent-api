from fastapi import APIRouter
from app.api.v1 import router as api_v1_router

router = APIRouter()

router.include_router(api_v1_router, prefix="/v1", tags=["api"])