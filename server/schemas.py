"""pydantic scheme"""

from typing import List, Optional

from pydantic import BaseModel


# --- Project ---
class ProjectBase(BaseModel):
    name: str
    description: str


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True


# --- Task ---
class TaskBase(BaseModel):
    name: str
    optimistic: float
    most_likely: float
    pessimistic: float
    project_id: int


class TaskCreate(TaskBase):
    predecessor_ids: List[int] = []


class Task(TaskBase):
    id: int
    predecessors: List[int] = []

    # Izračunata polja (nije u bazi)
    expected_time: float
    variance: float
    std_deviation: float

    class Config:
        orm_mode = True
