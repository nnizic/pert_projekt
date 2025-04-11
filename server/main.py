from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.routers import projects_router, tasks_router

from .database import init_db

app = FastAPI()

# omogućavanje CORS za frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # URL frontenda
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()  # kreira tablice ako ne postoje

app.include_router(projects_router)
app.include_router(tasks_router)
