from fastapi import APIRouter
from app.schemas import TaskCreate

router = APIRouter(prefix='/tasks', tags=['tasks'])

@router.post('/create-task')
def create_task(task: TaskCreate):
    return { 'message': 'New task is created' }