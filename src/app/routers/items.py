from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.app import schemas
from src.app import actions
from src.app import context_manager

router = APIRouter()


@router.get("/items", response_model=List[schemas.Item], status_code=status.HTTP_200_OK, tags=["simpleOps"])
def read_items(offset: int = 0, limit: int = 100, db: Session = Depends(context_manager.get_db)):
    items = actions.get_items(db, offset=offset, limit=limit)
    return items


@router.post("/items", status_code=status.HTTP_201_CREATED, tags=["simpleOps"])
def create_item(request: schemas.Item, db: Session = Depends(context_manager.get_db)):
    new_item = actions.create_new_item(
        db=db,
        title=request.title,
        description=request.description
    )
    return new_item


@router.get("/items/{id}", status_code=status.HTTP_200_OK, tags=["simpleOps"])
def read_item_by_id(item_id: int, db: Session = Depends(context_manager.get_db)):
    item = actions.get_item_by_id(db, item_id)

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The item with id {item_id} could not be found!"
        )

    return item


@router.delete("/items/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["simpleOps"])
def delete_item_by_id(item_id: int, db: Session = Depends(context_manager.get_db)):
    actions.delete_item_by_id(db=db, item_id=item_id)
