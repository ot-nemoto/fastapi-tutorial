"""path operationデコレータの依存関係
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/dependencies-in-path-operation-decorators/
"""

from fastapi import APIRouter, Depends, Header, HTTPException

router = APIRouter(
    prefix="/dependencies-in-path-operation-decorators",
    tags=["path operationデコレータの依存関係"],
)


async def verify_token(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: str = Header()):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


@router.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    """
    ヘッダーチェック
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -H 'x-token: fake-super-secret-token' \
        -H 'x-key: fake-super-secret-key' \
        'http://127.0.0.1:8000/dependencies/dependencies-in-path-operation-decorators/items/' | jq .
    """
    return [
        {
            "item": "Foo",
        },
        {
            "item": "Bar",
        },
    ]
