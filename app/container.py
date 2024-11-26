from dependency_injector import containers, providers

from app.db.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.chat_repository import ChatRepository
from app.services.auth_service import AuthService
from app.services.jwt_service import TokenServiceJWT
from app.services.user_service import UserService
from app.services.project_service import ProjectService
from app.services.chat_service import ChatService
from app.config import settings

DATABASE_URL = settings.DATABASE_URL
JWT_SECRET_KEY = settings.JWT_SECRET_KEY

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.auth_router",
            "app.api.v1.user_router",
            "app.api.v1.project_router",
            "app.api.v1.chat_router",
        ]
    )

    db = providers.Singleton(SessionLocal, db_url=DATABASE_URL)

    # Repositories
    user_repository = providers.Factory(
        UserRepository,
        db=db.provided.session,
    )
    project_repository = providers.Factory(
        ProjectRepository,
        db=db.provided.session,
    )
    chat_repository = providers.Factory(
        ChatRepository,
        db=db.provided.session,
    )

    # Services
    jwt_service = providers.Factory(
        TokenServiceJWT,
        secret_key=JWT_SECRET_KEY       
    )
    auth_service = providers.Factory(
        AuthService,
        user_repository=user_repository,
        token_service=jwt_service,
    )
    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
    project_service = providers.Factory(
        ProjectService,
        project_repository=project_repository,
        token_service=jwt_service,
    )
    chat_service = providers.Factory(
        ChatService,
        chat_repository=chat_repository,
        token_service=jwt_service,
    )
