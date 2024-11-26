from sqlalchemy.orm import Session
from typing import Callable, List
from contextlib import AbstractContextManager

from app.models.project import Project
from app.repositories.interfaces.project_repository_interface import ProjectRepositoryInterface

class ProjectRepository(ProjectRepositoryInterface):
    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    # Obtener un proyecto por su ID
    def get_by_id(self, project_id: str) -> Project:
        with self.db() as session:
            return session.query(Project).filter(Project.id == project_id).first()

    # Obtener todos los proyectos
    def get_all(self) -> List[Project]:
        with self.db() as session:
            return session.query(Project).all()

    # Obtener proyectos por propietario
    def get_by_owner(self, owner_id: str) -> List[Project]:
        with self.db() as session:
            return session.query(Project).filter(Project.owner_id == owner_id).all()

    # Crear un nuevo proyecto
    def create_project(self, project: Project) -> Project:
        with self.db() as session:
            session.add(project)
            session.commit()
            session.refresh(project)
        return project

    # Actualizar un proyecto existente
    def update_project(self, project_id: str, updates: dict) -> Project:
        with self.db() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                return None  # Manejar adecuadamente en la capa de servicio
            for key, value in updates.items():
                setattr(project, key, value)
            session.commit()
            session.refresh(project)
        return project

    # Eliminar un proyecto por su ID
    def delete_project(self, project_id: str) -> bool:
        with self.db() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                return False  # Manejar adecuadamente en la capa de servicio
            session.delete(project)
            session.commit()
        return True


    def get_all_projects(self):
        return self.get_all()

    def get_project_by_id(self, project_id: int):
        return self.get_by_id(project_id)

    def create_project(self, project_data: dict):
        project = Project(**project_data)
        return self.create_project(project)

    def update_project(self, project_id: int, updates: dict):
        return self.update_project(project_id, updates)

    def delete_project(self, project_id: int):
        return self.delete_project(project_id)