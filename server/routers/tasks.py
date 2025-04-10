"""API za zadatke"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models
from .. import schemas
from ..database import SessionLocal, get_db
from ..services import build_task_graph

router = APIRouter(prefix="/tasks", tags=["tasks"])


def calculate_pert(task):
    te = (task.optimistic + 4 * task.most_likely + task.pessimistic) / 6
    variance = ((task.pessimistic - task.optimistic) / 6) ** 2
    return {
        "id": task.id,
        "name": task.name,
        "optimistic": task.optimistic,
        "most_likely": task.most_likely,
        "pessimistic": task.pessimistic,
        "project_id": task.project_id,
        "predecessors": [t.id for t in task.predecessors],
        "expected_time": te,
        "variance": variance,
        "std_deviation": variance**0.5,
    }


@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(
        name=task.name,
        optimistic=task.optimistic,
        most_likely=task.most_likely,
        pessimistic=task.pessimistic,
        project_id=task.project_id,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    # Dodaj prethodnike
    for pred_id in task.predecessor_ids:
        pred_task = db.query(models.Task).get(pred_id)
        if not pred_task:
            raise HTTPException(
                status_code=404, detail=f"Predecessor ID {pred_id} not found"
            )
        db_task.predecessors.append(pred_task)

    db.commit()

    return calculate_pert(db_task)  # za POST


@router.get("/", response_model=list[schemas.Task])
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return [calculate_pert(t) for t in tasks]  # za GET


# testni privremeni endpoint
@router.get("/projects/{project_id}/graph")
def get_task_graph(project_id: int, db: Session = Depends(get_db)):

    graph = build_task_graph(project_id, db)
    return {
        task_id: {
            "name": data["task"].name,
            "predecessors": data["predecessors"],
            "successors": data["successors"],
        }
        for task_id, data in graph.items()
    }
