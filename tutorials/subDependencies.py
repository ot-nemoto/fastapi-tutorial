"""サブ依存関係
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/sub-dependencies/
"""

from typing import Union

from fastapi import APIRouter, Cookie, Depends

router = APIRouter(
    prefix="/sub-dependencies",
    tags=["サブ依存関係"],
)


def query_extractor(q: Union[str, None] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor),
    last_query: Union[str, None] = Cookie(default=None),
):
    print(q)
    print(last_query)
    if not q:
        return last_query
    return q


@router.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    """
    Cookieを取得
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -b 'last_query=last_query;' \
        'http://127.0.0.1:8000/dependencies/sub-dependencies/items/?q=q' | jq .
    curl -s -XGET \
        -H 'accept: application/json' \
        -b 'last_query=last_query;' \
        'http://127.0.0.1:8000/dependencies/sub-dependencies/items/' | jq .
    """
    return {
        "q_or_cookie": query_or_default,
    }
