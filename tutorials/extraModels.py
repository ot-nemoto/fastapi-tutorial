"""モデル - より詳しく
ref https://fastapi.tiangolo.com/ja/tutorial/extra-models/
"""

from typing import Dict, List, Union
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/extra-models",
    tags=["モデル - より詳しく"],
)


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@router.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    """
    UserIn -> UserInDB -> UserOut<br>
    - UserInDB: `password` を削除し、`hashed_password` に変換<br>
    - UserOut: `hashed_password` を削除し返す
    """
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car",
    },
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@router.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    """
    継承したモデルで取得
    """
    return items[item_id]


@router.get("/items/", response_model=List[Union[PlaneItem, CarItem]])
async def read_items():
    """
    *List* で取得
    """
    return items.values()


@router.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
    """
    *Dict* で取得
    """
    return {
        "foo": 2.3,
        "bar": 3.4,
    }
