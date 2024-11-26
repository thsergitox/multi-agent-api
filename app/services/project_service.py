from app.repositories.project_repository import ProjectRepository
from app.repositories.interfaces.project_repository_interface import ProjectRepositoryInterface
from app.services.interfaces.token_service_interface import TokenServiceInterface
from app.models.project import Project

class ProjectService:
    def __init__(self, project_repository: ProjectRepositoryInterface, token_service: TokenServiceInterface):
        self.project_repository = project_repository
        self.token_service = token_service

    def get_project(self, project_id: str):
        project = self.project_repository.get_by_id(project_id)
        if not project:
            raise ValueError(f"Project with ID {project_id} not found")
        return project

    def create_project(self, project_data: dict):
        try:
            if 'papers' not in project_data:
                project_data['papers'] = []

            # Verify token and get user_id
            token_data = self.token_service.verify_token(project_data['access_token'])
            if not token_data or 'sub' not in token_data:
                raise ValueError("Invalid token")
            
            owner_id = token_data['sub']
            
            # Convert dict to Project instance
            project = Project(
                owner_id=owner_id,
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
