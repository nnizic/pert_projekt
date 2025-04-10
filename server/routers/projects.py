"""API za projekte"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db  # koristiš već definirani globalni get_db

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(
        name=project.name,
        description=project.description,  # ako koristiš description u schemi/modelu
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.get("/", response_model=list[schemas.Project])
def list_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()


@router.get("/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.delete("/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return project
