from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from mypackage import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    statement = select(models.Item).offset(skip).limit(limit)
    return db.exec(statement).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    statement = select(models.User).offset(skip).limit(limit)
    return db.exec(statement).all()


def get_user_by_email(db: Session, email: str):
    statement = select(models.User).where(models.User.email == email)
    return db.exec(statement).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_for_user(db: Session, user_id: int, item: schemas.ItemCreate):
    db_user = db.get(models.User, user_id)

    if not db_user:
        raise NoResultFound(f"User with id {user_id} not found")

    db_item = models.Item(**item.model_dump(), owner=db_user)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
