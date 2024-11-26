from sqlalchemy.orm import Session
from typing import Callable, List
from contextlib import AbstractContextManager

from app.models.project import Project
from app.repositories.interfaces.project_repository_interface import ProjectRepositoryInterface

class ProjectRepository(ProjectRepositoryInterface):
    def __init__(self, db: Callable[..., AbstractContextManager[Session]]):
        self.db = db

    def get_by_id(self, project_id: str) -> Project:
        with self.db() as session:
            return session.query(Project).filter(Project.id == project_id).first()

    def get_all(self) -> List[Project]:
        with self.db() as session:
            return session.query(Project).all()

    def get_by_owner(self, owner_id: str) -> List[Project]:
        with self.db() as session:
            return session.query(Project).filter(Project.owner_id == owner_id).all()

    def create_project(self, project: Project) -> Project:
        with self.db() as session:
            session.add(project)
            session.commit()
            session.refresh(project)
            return project

    def update_project(self, project_id: str, updates: dict) -> Project:
        with self.db() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                return None
            for key, value in updates.items():
                setattr(project, key, value)
            session.commit()
            session.refresh(project)
            return project

    def delete_project(self, project_id: str) -> bool:
        with self.db() as session:
            project = session.query(Project).filter(Project.id == project_id).first()
            if not project:
                return False
            session.delete(project)
            session.commit()
            return True

    # Alias methods
    get_all_projects = get_all
    get_project_by_id = get_by_id