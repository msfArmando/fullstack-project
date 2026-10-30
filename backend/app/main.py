from fastapi import FastAPI
from http import HTTPStatus
from .routers import task
from .models import Task

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK)
async def root():
    return { 'message': 'backend in running' }

app.include_router(task.router)