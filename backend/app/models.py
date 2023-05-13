from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Text, ForeignKey
from sqlalchemy_utils import EmailType, ChoiceType
from sqlalchemy.orm import relationship

from .database import Base
from . import enums


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(EmailType, nullable=False, unique=True)
    password = Column(String, nullable=False)
    dob = Column(String)
    is_active = Column(Boolean, default=True)
    gender = Column(ChoiceType(enums.Gender, impl=String()))
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime)

    todos = relationship("TodoModel", back_populates="owner")


class TodoModel(Base):
    __tablename__ = "todos"

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    status = Column(ChoiceType(enums.Status, impl=String()), default=enums.Status.TODO, nullable=False)
    priority = Column(ChoiceType(enums.Priority, impl=Integer()), default=enums.Priority.REGULAR, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime)

    owner = relationship("UserModel", back_populates="todos")
