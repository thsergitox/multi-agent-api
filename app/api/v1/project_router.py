from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from app.schemas.project import ProjectSchema, ProjectCreateSchema, ProjectUpdateSchema
from app.services.project_service import ProjectService
from app.container import Container

router = APIRouter()

@router.get("/")
@inject
def list_projects(project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.get_all_projects()

@router.post("/")
@inject
def create_project(project_data: ProjectCreateSchema, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.create_project(project_data.dict())

@router.get("/{project_id}")
@inject
def get_project(project_id: str, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.get_project(project_id)

@router.put("/{project_id}")
@inject
def update_project(project_id: str, updates: ProjectUpdateSchema, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.update_project(project_id, updates.dict())

@router.delete("/{project_id}")
@inject
def delete_project(project_id: str, project_service: ProjectService = Depends(Provide[Container.project_service])):
    return project_service.delete_project(project_id)

