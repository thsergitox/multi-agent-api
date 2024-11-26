from app.repositories.project_repository import ProjectRepository
from app.repositories.interfaces.project_repository_interface import ProjectRepositoryInterface
from app.models.project import Project

class ProjectService:
    def __init__(self, project_repository: ProjectRepositoryInterface):
        self.project_repository = project_repository

    def get_project(self, project_id: str):
        project = self.project_repository.get_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found")
        return project

    def create_project(self, project_data: dict):
        try:
            if 'papers' not in project_data:
                project_data['papers'] = []
            
            # Convert dict to Project instance
            project = Project(
                owner_id=project_data['owner_id'],
                title=project_data['title'],
                description=project_data.get('description'),
                is_public=project_data.get('is_public', True),
                papers=project_data.get('papers', [])
            )
            return self.project_repository.create_project(project)
        except Exception as e:
            raise ValueError(f"Error creating project: {str(e)}")

    def update_project(self, project_id: str, updates: dict):
        project = self.project_repository.update_project(project_id, updates)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found")
        return project

    def delete_project(self, project_id: str):
        success = self.project_repository.delete_project(project_id)
        if not success:
            raise ValueError(f"Project with ID {project_id} not found")
        return success
    

    def get_all_projects(self):
        return self.project_repository.get_all_projects()
