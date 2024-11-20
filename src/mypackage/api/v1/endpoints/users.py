from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from mypackage import crud, database, schemas

router = APIRouter(tags=["users"])


@router.get("/users/", response_model=List[schemas.User])
def read_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_session)
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post(
    "/users/",
    response_model=schemas.User,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_session)):
    try:
        db_user = crud.create_user(db, user)
    except IntegrityError:
        db.rollback()
        existing_user = crud.get_user_by_email(db=db, email=user.email)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Email '{existing_user.email}' already registered",
        )

    return db_user
