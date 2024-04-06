"""ボディ - ネストされたモデル
ref https://fastapi.tiangolo.com/ja/tutorial/body-nested-models/
"""

from typing import Set, Union, List, Dict
from fastapi import APIRouter, Body
from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    images: Union[List[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


router = APIRouter(
    prefix="/body-nested-models",
    tags=["ボディ - ネストされたモデル"],
)


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@router.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@router.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


@router.post("/index-weights/")
async def create_index_weights(
    weights: Dict[int, float] = Body(example={"1": 1.23, "100": -0.2})
):
    return weights
