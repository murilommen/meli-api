from typing import Optional
from pydantic import BaseModel


class BaseItem(BaseModel):
    class Config:
        orm_mode = True


class Item(BaseItem):
    title: str
    description: Optional[str] = None
