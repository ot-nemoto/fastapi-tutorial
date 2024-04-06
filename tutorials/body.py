"""リクエストボディ
ref https://fastapi.tiangolo.com/ja/tutorial/body/
"""

from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix="/body",
    tags=["リクエストボディ"],
)


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


# @router.post("/items/")
# async def create_item(item: Item):
#     return item


@router.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# @router.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
