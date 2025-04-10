"""perth grafovi"""

from sqlalchemy.orm import Session

from .. import models


def build_task_graph(project_id: int, db: Session):
    tasks = db.query(models.Task).filter(models.Task.project_id == project_id).all()

    graph = {}

    # Inicijalizacija čvorova
    for task in tasks:
        graph[task.id] = {
            "task": task,
            "predecessors": [t.id for t in task.predecessors],
            "successors": [],  # popunjavamo u sljedećem koraku
        }

    # Popunjavanje successor lista
    for task_id, data in graph.items():
        for pred_id in data["predecessors"]:
            if pred_id in graph:
                graph[pred_id]["successors"].append(task_id)

    return graph
