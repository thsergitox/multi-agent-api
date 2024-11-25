from fastapi import APIRouter
from app.api.v1.auth_router import router as api_router
from app.api.v1.latex_router import router as latex_router

router = APIRouter()

router.include_router(api_router, prefix="/auth", tags=["auth"])
router.include_router(latex_router, prefix="/latex", tags=["latex"])