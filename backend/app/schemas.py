from datetime import date

from pydantic import BaseModel
from . import enums


class TodoBase(BaseModel):
    title: str
    description: str | None = None


class TodoCreate(TodoBase):
    owner_id: int
    priority: int = 1


class Todo(TodoBase):
    status: str
    priority: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    email: str
    password: str
    dob: date = None
    gender: enums.Gender = None


class User(UserBase):
    id: int
    is_active: bool
    dob: date
    gender: enums.Gender
    todos: list[Todo] = []

    class Config:
        orm_mode = True
