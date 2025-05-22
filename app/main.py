from fastapi import FastAPI
from app.api import students_router  

app = FastAPI()

app.include_router(students_router.router)