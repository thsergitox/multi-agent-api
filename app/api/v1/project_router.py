from fastapi import APIRouter, Depends, HTTPException  
from dependency_injector.wiring import Provide, inject
from app.schemas.project import ProjectSchema, ProjectCreateSchema, ProjectUpdateSchema, UserProjectsRequestSchema
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
    try:
        return project_service.create_project(project_data.model_dump())
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error creating project: {str(e)}"
        )

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

@router.post("/get_by_user", response_model=list[ProjectSchema])
@inject
def get_projects_by_user(request: UserProjectsRequestSchema, project_service: ProjectService = Depends(Provide[Container.project_service])):
    try:
        return project_service.get_projects_by_user(request.access_token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

