from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema


class UserNotFoundException(Exception):
    """Excepción personalizada para cuando un usuario no es encontrado."""
    def __init__(self, user_id: str):
        self.message = f"User with ID {user_id} not found"
        super().__init__(self.message)


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: str) -> UserSchema:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)
        return UserSchema.from_orm(user)

    def create_user(self, user_data: UserCreateSchema) -> UserSchema:
        new_user = User(**user_data.dict())
        created_user = self.user_repository.create_user(new_user)
        return UserSchema.from_orm(created_user)

    def update_user(self, user_id: str, updates: UserUpdateSchema) -> UserSchema:
        updates_dict = updates.dict(exclude_unset=True)
        updated_user = self.user_repository.update_user(user_id, updates_dict)
        if not updated_user:
            raise UserNotFoundException(user_id)
        return UserSchema.from_orm(updated_user)

    def delete_user(self, user_id: str) -> bool:
        success = self.user_repository.delete_user(user_id)
        if not success:
            raise UserNotFoundException(user_id)
        return success
    
    def get_all_users(self) -> list[UserSchema]:
        users = self.user_repository.get_all_users()
        return [UserSchema.from_orm(user) for user in users]
