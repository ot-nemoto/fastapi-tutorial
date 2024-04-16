"""Global Dependencies
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/global-dependencies/
"""

from fastapi import APIRouter, Header, HTTPException, Request
from typing_extensions import Annotated

import main

router = APIRouter(
    prefix="/global-dependencies",
    tags=["Global Dependencies"],
)


async def verify_token(x_token: Annotated[str, Header()], request: Request):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()], request: Request):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


# main.app.dependency_overrides[main.verify_token] = verify_token
# main.app.dependency_overrides[main.verify_key] = verify_key


@router.get("/items/")
async def read_items():
    """
    Global Dependenciesの検証<br>
    以下のコメント外す
    ```
    # main.app.dependency_overrides[main.verify_token] = verify_token
    # main.app.dependency_overrides[main.verify_key] = verify_key
    ```
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -H 'x-token: fake-super-secret-token' \
        -H 'x-key: fake-super-secret-key' \
        'http://127.0.0.1:8000/dependencies/global-dependencies/items/' | jq .
    """
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


@router.get("/users/")
async def read_users():
    """
    Global Dependenciesの検証<br>
    以下のコメント外す
    ```
    # main.app.dependency_overrides[main.verify_token] = verify_token
    # main.app.dependency_overrides[main.verify_key] = verify_key
    ```
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -H 'x-token: fake-super-secret-token' \
        -H 'x-key: fake-super-secret-key' \
        'http://127.0.0.1:8000/dependencies/global-dependencies/users/' | jq .
    """
    return [{"username": "Rick"}, {"username": "Morty"}]
