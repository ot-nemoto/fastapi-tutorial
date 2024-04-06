"""ヘッダーのパラメータ
ref https://fastapi.tiangolo.com/ja/tutorial/header-params/
"""

from typing import Union, List
from fastapi import APIRouter, Header

router = APIRouter(
    prefix="/header-params",
    tags=["ヘッダーのパラメータ"],
)


@router.get("/case01/")
async def read_items(
    user_agent: Union[str, None] = Header(default=None),
):
    """
    User-Agentを取得
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0' \
        'http://127.0.0.1:8000/header-params/case01/' | jq .
    """
    return {
        "User-Agent": user_agent,
    }


@router.get("/case02/")
async def read_items(
    user_agent: Union[str, None] = Header(default=None, convert_underscores=False),
):
    """
    アンダースコアからハイフンへの自動変換を無効
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0' \
        'http://127.0.0.1:8000/header-params/case02/' | jq .
    """
    return {
        "User-Agent": user_agent,
    }


@router.get("/case03/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    """
    ヘッダーの重複
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        -H 'X-Token: bar' \
        -H 'X-Token: foo' \
        'http://127.0.0.1:8000/header-params/case03/' | jq .
    """
    return {
        "X-Token values": x_token,
    }
