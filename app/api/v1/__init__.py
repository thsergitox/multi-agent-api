from fastapi import APIRouter
from app.api.v1.auth_router import router as auth_router
from app.api.v1.latex_router import router as latex_router
from app.api.v1.user_router import router as user_router
from app.api.v1.project_router import router as project_router
from app.api.v1.chat_router import router as chat_router
from app.api.v1.ai_router import router as ai_router

router = APIRouter()

# Auth and Latex Routes
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(latex_router, prefix="/latex", tags=["latex"])

# Users Routes
router.include_router(user_router, prefix="/users", tags=["users"])

# Projects Routes
router.include_router(project_router, prefix="/projects", tags=["projects"])

# Chat Routes
router.include_router(chat_router, prefix="/chat", tags=["chat"])

router.include_router(ai_router, prefix="/ai", tags=["ai"])