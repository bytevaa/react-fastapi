from typing import Optional
import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Category:
    name: str
    color: str

@strawberry.type
class Task:
    id: int
    title: str
    description: str
    is_completed: bool
    category: Optional[Category] = None


tasks: list[Task] = [
    Task(
        id=1,
        title="Изучить Graphql",
        description="Продолжаю обучение",
        is_completed= False,
        category=Category(name='Учеба', color='#3b82f6')
    ),
    Task(
        id=2,
        title="Запустить React",
        description="Попытка записи",
        is_completed= True,
        category=Category(name='Разработка', color='#3b82f6')
    )
]
next_task_id = 3

@strawberry.type
class Query:
    @strawberry.field
    def all_tasks(self) -> list[Task]:
        return tasks

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_task(self , title:str) -> Task:
        global next_task_id
        clean_title = title.strip()
        if len(clean_title) < 3:
            raise ValueError("Название задачи должно содержать как минимкм 3 символа")
        task = Task(
            id=next_task_id,
            title=clean_title,
            description="",
            is_completed=False,
            category=Category(name="Без категории", color="64748b"),
        )
        next_task_id += 1
        tasks.append(task)
        return task
    
    @strawberry.mutation
    def complete_task(self , task_id: int) -> Optional[Task]:
        for task in tasks:
            if task.id == task_id:
                task.is_completed = True
                return task
        return None
    
    @strawberry.mutation
    def delete_task(self, task_id: int) -> bool:
        for index , task in enumerate(tasks):
            if task.id == task_id:
                del tasks[index]
                return True
        return False

    
    


schema = strawberry.Schema(query=Query , mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins= ['http://localhost:5173' , 'http://127.0.0.1:5173'] , allow_credentials= True , allow_methods=['*'] , allow_headers=['*'])


app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "Task Manager GraphQL API", "graphql": "/graphql"}
