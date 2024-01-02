from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from mypackage import crud, schemas, database

router = APIRouter(tags=["items"])


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.post(
    "/items/", response_model=schemas.ItemCreate, status_code=status.HTTP_201_CREATED
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = crud.create_item(db, item)
    return db_item
