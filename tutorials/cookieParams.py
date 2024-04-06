"""クッキーのパラメータ
ref https://fastapi.tiangolo.com/ja/tutorial/cookie-params/
"""

from typing import Union
from fastapi import APIRouter, Cookie

router = APIRouter(
    prefix="/cookie-params",
    tags=["クッキーのパラメータ"],
)


@router.get("/case01/")
async def read_items(
    name: Union[str, None] = Cookie(default=None),
    prefecture: Union[str, None] = Cookie(default=None),
    city: Union[str, None] = Cookie(default=None),
):
    """
    Cookieを取得
    """
    """
    curl -s -XGET \
        -b 'name=ot-nemoto; prefecture=saitama; city=saitama;' \
        'http://127.0.0.1:8000/cookie-params/case01/' | jq .
    """
    return {
        "name": name,
        "prefecture": prefecture,
        "city": city,
    }
