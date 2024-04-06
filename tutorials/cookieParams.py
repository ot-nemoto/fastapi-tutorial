"""クッキーのパラメータ
ref https://fastapi.tiangolo.com/ja/tutorial/cookie-params/
"""

from typing import Union
from fastapi import APIRouter, Body, Cookie

router = APIRouter(
    prefix="/cookie-params",
    tags=["クッキーのパラメータ"],
)


@router.get("/items/")
async def read_items(ads_id: Union[str, None] = Cookie(default=None)):
    return {"ads_id": ads_id}
