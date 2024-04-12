"""JSON互換エンコーダ
ref https://fastapi.tiangolo.com/ja/tutorial/encoder/
"""

from datetime import datetime
from typing import Union

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter(
    prefix="/encoder",
    tags=["JSON互換エンコーダ"],
)

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


@router.put("/items/{id}")
def update_item(id: str, item: Item):
    rt = {"id": id}
    if id not in fake_db.keys():
        json_compatible_item_data = jsonable_encoder(item)
        fake_db[id] = json_compatible_item_data
    return rt | {"item": fake_db[id]}
