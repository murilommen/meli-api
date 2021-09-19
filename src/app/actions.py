from sqlalchemy.orm import Session

from src.app import models


def create_new_item(db: Session, title: str, description: str):
    new_item = models.Item(title=title, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def get_items(db: Session, offset: int, limit: int):
    return db.query(models.Item).offset(offset).limit(limit).all()


def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def delete_item_by_id(db: Session, item_id: int):
    db.query(models.Item).filter(models.Item.id == item_id).delete(synchronize_session=False)
    db.commit()


