# app/repositories/interfaces/project_repository_interface.py

from abc import ABC, abstractmethod

class ProjectRepositoryInterface(ABC):
    @abstractmethod
    def get_all_projects(self):
        pass

    @abstractmethod
    def get_project_by_id(self, project_id: int):
        pass

    @abstractmethod
    def create_project(self, project_data: dict):
        pass

    @abstractmethod
    def update_project(self, project_id: int, updates: dict):
        pass

    @abstractmethod
    def delete_project(self, project_id: int):
        pass
