"""API za projekte"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from .. import models
from ..database import SessionLocal

router = APIRouter(prefix="/projects", tags=["projects"])


# Dependency za session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(name=project.name)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.get("/", response_model=list[schemas.Project])
def list_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()
