"""ボディ - 複数のパラメータ
ref https://fastapi.tiangolo.com/ja/tutorial/body-multiple-params/
"""

from typing import Union
from fastapi import APIRouter, Body
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


router = APIRouter(
    prefix="/body-multiple-params",
    tags=["ボディ - 複数のパラメータ"],
)


@router.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(gt=0),
    q: Union[str, None] = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


# @router.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(embed=True)):
#     """
#     単一のボディパラメータの埋め込み
#     """
#     results = {"item_id": item_id, "item": item}
#     return results
