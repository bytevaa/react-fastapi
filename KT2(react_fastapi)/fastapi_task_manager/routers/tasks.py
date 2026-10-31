from fastapi import APIRouter, HTTPException, status
from models.task import Task, TaskCreate, TaskOut

router = APIRouter(prefix="/tasks", tags=["tasks"])

_tasks: list[Task] = []
_next_id = 1

@router.get("", response_model=list[TaskOut])
def get_tasks():
    return _tasks

@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    global _next_id
    task = Task(id=_next_id, **task_data.model_dump())
    _tasks.append(task)
    _next_id += 1
    return task

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int):
    for task in _tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")
