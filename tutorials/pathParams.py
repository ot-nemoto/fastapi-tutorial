"""パスパラメータ
ref https://fastapi.tiangolo.com/ja/tutorial/path-params/
"""

from enum import Enum
from fastapi import APIRouter


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


router = APIRouter(
    prefix="/path-params",
    tags=["パスパラメータ"],
)


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
