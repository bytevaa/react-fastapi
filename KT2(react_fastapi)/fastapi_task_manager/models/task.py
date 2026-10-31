from pydantic import BaseModel, Field, field_validator

class Category(BaseModel):
    name: str
    color: str

class TaskCreate(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    category: Category

    @field_validator("title")
    @classmethod
    def title_min_length(cls, value: str) -> str:
        if len(value.strip()) < 3:
            raise ValueError("Название задачи должно содержать минимум 3 символа")
        return value

class Task(TaskCreate):
    id: int
    internal_note: str = "Служебная заметка"

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool
    category: Category
