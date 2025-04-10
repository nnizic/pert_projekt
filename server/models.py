from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Pomoćna tablica za many-to-many između zadataka (predecessors)
task_dependencies = Table(
    "task_dependencies",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id")),
    Column("depends_on_id", Integer, ForeignKey("tasks.id")),
)


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="project")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    optimistic = Column(Float)
    most_likely = Column(Float)
    pessimistic = Column(Float)

    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="tasks")

    predecessors = relationship(
        "Task",
        secondary=task_dependencies,
        primaryjoin=id == task_dependencies.c.task_id,
        secondaryjoin=id == task_dependencies.c.depends_on_id,
        backref="dependents",
    )
