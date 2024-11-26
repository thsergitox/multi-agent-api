from sqlalchemy.orm import Session
from typing import Callable
from contextlib import AbstractContextManager

from app.models.user import User
from app.repositories.interfaces.user_repository_interface import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):   
    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    # Obtener un usuario por su ID
    def get_by_id(self, user_id: str) -> User:
        with self.db() as session:
            return session.query(User).filter(User.id == user_id).first()

    # Obtener un usuario por su email
    def get_by_email(self, email: str) -> User:
        with self.db() as session:
            return session.query(User).filter(User.email == email).first()

    # Crear un nuevo usuario
    def create_user(self, user: User) -> User:
        with self.db() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    # Actualizar un usuario existente
    def update_user(self, user_id: str, updates: dict) -> User:
        with self.db() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                return None  # Manejar de forma adecuada en la capa de servicio
            for key, value in updates.items():
                setattr(user, key, value)  # Aplicar los cambios
            session.commit()
            session.refresh(user)
        return user

    # Eliminar un usuario
    def delete_user(self, user_id: str) -> bool:
        with self.db() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                return False  # Manejar de forma adecuada en la capa de servicio
            
    def get_all_users(self) -> list[User]:
        with self.db() as session:
            return session.query(User).all()
