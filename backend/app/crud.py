from sqlalchemy.orm import Session
from app.models import UserModel, TodoModel
from app.schemas import UserCreate, TodoCreate


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session):
    return db.query(UserModel).all()


def create_user(db: Session, user: UserCreate):
    db_user = UserModel(name=user.name, email=user.email, password=user.password, dob=user.dob, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_todos(db: Session):
    return db.query(TodoModel).all()


def get_user_todos(db: Session, owner_id: int):
    return db.query(TodoModel).filter(owner_id=owner_id)


def create_todo(db: Session, todo: TodoCreate):
    db_todo = TodoModel(title=todo.title, description=todo.description, owner_id=todo.owner_id, priority=todo.priority)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
