"""レスポンスモデル
ref https://fastapi.tiangolo.com/ja/tutorial/response-model/
"""

from typing import Any, List, Union
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/response-model",
    tags=["レスポンスモデル"],
)


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {
        "name": "Foo",
        "price": 50.2,
    },
    "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2,
    },
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": [],
    },
}


@router.post(
    "/items/",
    response_model=Item,
)
async def create_item(item: Item) -> Any:
    """
    レスポンスにモデルを指定<br>
    ```
    response_model=Item,
    ```
    """
    return item


@router.get(
    "/items/",
    response_model=List[Item],
)
async def read_items() -> Any:
    """
    レスポンスにリストを指定<br>
    ```
    response_model=List[Item],
    ```
    """
    return items.values()


@router.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
)
async def read_item(item_id: str):
    """
    レスポンスにデフォルト値は含まない<br>
    ```
    response_model=Item,
    response_model_exclude_unset=True,
    ```
    """
    return items[item_id]


@router.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    """
    レスポンス（Item）の `name` と `description` のみ含める<br>
    ```
    response_model=Item,
    response_model_include={"name", "description"},
    ```
    """
    return items[item_id]


@router.get(
    "/items/{item_id}/public",
    response_model=Item,
    response_model_exclude={"tax"},
)
async def read_item_public_data(item_id: str):
    """
    レスポンス（Item）に `tax` を含めない<br>
    ```
    response_model=Item,
    response_model_exclude={"tax"},
    ```
    """
    return items[item_id]


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@router.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    """
    出力モデルで宣言されていない入力データはフィルタリングして出力される
    - 入力モデル: `UserIn`<br>
    - 出力モデル: `UserOut`<br>
    """
    return user
