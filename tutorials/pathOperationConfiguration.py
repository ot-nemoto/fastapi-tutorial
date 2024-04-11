"""Path Operationの設定
ref https://fastapi.tiangolo.com/ja/tutorial/path-operation-configuration/
"""

from typing import Set, Union

from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/path-operation-configuration",
    tags=["Path Operationの設定"],
)


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@router.post("/case01/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    return item


@router.post("/case02/items/", response_model=Item, tags=["items"])
async def create_item(item: Item):
    return item


@router.get("/case02/items/", tags=["items"])
async def read_items():
    return [
        {
            "name": "Foo",
            "price": 42.0,
        }
    ]


@router.get("/case02/users/", tags=["users"])
async def read_users():
    return [
        {
            "username": "johndoe",
        }
    ]


@router.post(
    "/case03/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    return item


@router.post(
    "/case04/items/",
    response_model=Item,
    summary="Create an item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@router.post(
    "/case05/items/",
    response_model=Item,
    summary="Create an item",
    response_description="The created item",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@router.get(
    "/case06/elements/",
    tags=["items"],
    deprecated=True,
)
async def read_elements():
    return [
        {
            "item_id": "Foo",
        }
    ]
