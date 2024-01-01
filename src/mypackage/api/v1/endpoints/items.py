from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from mypackage import crud, schemas
from mypackage.database import get_db

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)
