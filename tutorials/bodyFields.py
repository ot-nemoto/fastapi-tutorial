"""ボディ - フィールド
ref https://fastapi.tiangolo.com/ja/tutorial/body-fields/
"""

from typing import Union
from fastapi import APIRouter, Body
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/body-fields",
    tags=["ボディ - フィールド"],
)


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
