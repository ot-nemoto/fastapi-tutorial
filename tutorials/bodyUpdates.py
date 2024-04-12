"""ボディ - 更新
ref https://fastapi.tiangolo.com/ja/tutorial/body-updates/
"""

from typing import List, Union

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

router = APIRouter(
    prefix="/body-updates",
    tags=["ボディ - 更新"],
)


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@router.put("/case01/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    """
    PUTによる置換での更新<br>
    Request bodyが以下の場合、他の項目はデフォルト値で更新<br>
    ```
    {
        "name": "ot-nemoto"
    }
    ```
    """
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


@router.patch("/case02/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    """
    PATCHによる部分的な更新<br>
    Request bodyが以下の場合、他の項目は既存のまま更新しない<br>
    ```
    {
        "name": "ot-nemoto"
    }
    """
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
