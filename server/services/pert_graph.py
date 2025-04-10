"""PERT graf funkcije"""

from sqlalchemy.orm import Session

from .. import models


def calculate_pert(task):
    """
    Izračunava PERT za zadatak koristeći optimističko, najvjerojatnije i pesimističko vrijeme.
    Formula za očekivano trajanje: TE = (O + 4M + P) / 6
    """
    optimistic = task.optimistic
    most_likely = task.most_likely
    pessimistic = task.pessimistic

    te = (optimistic + 4 * most_likely + pessimistic) / 6
    variance = ((pessimistic - optimistic) / 6) ** 2
    std_deviation = variance**0.5

    return {
        "id": task.id,
        "name": task.name,
        "expected_time": te,
        "variance": variance,
        "std_deviation": std_deviation,
    }


def build_task_graph(project_id: int, db: Session):
    """
    Izgrađuje graf zadataka s predecessorima i successorima.
    """
    tasks = db.query(models.Task).filter(models.Task.project_id == project_id).all()
    graph = {}

    for task in tasks:
        graph[task.id] = {
            "task": task,
            "predecessors": [t.id for t in task.predecessors],
            "successors": [],
            "early_start": 0,
            "early_finish": 0,
            "late_start": 0,
            "late_finish": 0,
        }

    for task_id, data in graph.items():
        for pred_id in data["predecessors"]:
            if pred_id in graph:
                graph[pred_id]["successors"].append(task_id)

    return graph


def forward_pass(graph: dict):
    """
    Računa najranije početke i završetke za svaki zadatak.
    """
    sorted_tasks = topological_sort(graph)

    for task_id in sorted_tasks:
        data = graph[task_id]
        preds = data["predecessors"]

        if preds:
            data["early_start"] = max(graph[p]["early_finish"] for p in preds)
        else:
            data["early_start"] = 0

        duration = data["task"].most_likely
        if duration is None:
            raise ValueError(f"Zadatak {task_id} nema most_likely trajanje.")

        data["early_finish"] = data["early_start"] + duration

    return graph


def backward_pass(graph: dict):
    """
    Računa najkasnije početke i završetke za svaki zadatak.
    """
    sorted_tasks = topological_sort(graph)[::-1]

    # Inicijalizacija late_finish za završne zadatke
    for task_id in sorted_tasks:
        data = graph[task_id]
        if not data["successors"]:
            data["late_finish"] = data["early_finish"]
            data["late_start"] = data["late_finish"] - data["task"].most_likely

    for task_id in sorted_tasks:
        data = graph[task_id]
        succs = data["successors"]

        if succs:
            # Ako neki successor još nema late_start, preskoči dok se ne izračuna
            if any(graph[s]["late_start"] is None for s in succs):
                raise ValueError(
                    f"Task {task_id} successors have undefined 'late_start' values."
                )

            data["late_finish"] = min(graph[s]["late_start"] for s in succs)

        if data["late_finish"] is not None:
            data["late_start"] = data["late_finish"] - data["task"].most_likely
        else:
            raise ValueError(
                f"Task {task_id} does not have a valid 'late_finish' value."
            )

    return graph


def get_critical_path(graph: dict):
    """
    Vraća popis ID-eva zadataka koji su na kritičnom putu.
    """
    critical_path = []

    for task_id, data in graph.items():
        if data["early_start"] == data["late_start"]:
            critical_path.append(task_id)

    return critical_path


def topological_sort(graph: dict):
    """
    Topološki sort grafa za ispravno izvođenje forward/backward pasa.
    """
    visited = set()
    result = []

    def dfs(task_id):
        if task_id in visited:
            return
        visited.add(task_id)
        for succ in graph[task_id]["successors"]:
            dfs(succ)
        result.insert(0, task_id)

    for task_id in graph:
        dfs(task_id)

    return result
