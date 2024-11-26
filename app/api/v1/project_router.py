from fastapi import APIRouter, Depends
from app.schemas.project import ProjectSchema, ProjectCreateSchema, ProjectUpdateSchema
from app.services.project_service import ProjectService

router = APIRouter()

@router.get("/")
def list_projects(project_service: ProjectService = Depends()):
    return project_service.get_all_projects()

@router.post("/")
def create_project(project_data: ProjectCreateSchema, project_service: ProjectService = Depends()):
    return project_service.create_project(project_data.dict())

@router.get("/{project_id}")
def get_project(project_id: str, project_service: ProjectService = Depends()):
    return project_service.get_project(project_id)

@router.put("/{project_id}")
def update_project(project_id: str, updates: ProjectUpdateSchema, project_service: ProjectService = Depends()):
    return project_service.update_project(project_id, updates.dict())

@router.delete("/{project_id}")
def delete_project(project_id: str, project_service: ProjectService = Depends()):
    return project_service.delete_project(project_id)
