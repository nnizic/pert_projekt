from fastapi import FastAPI

from .database import init_db
from server.routers import projects_router, tasks_router

app = FastAPI()

init_db()  # kreira tablice ako ne postoje

app.include_router(projects_router)
app.include_router(tasks_router)
