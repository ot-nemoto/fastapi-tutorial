"""エラーハンドリング
ref https://fastapi.tiangolo.com/ja/tutorial/handling-errors/
"""

from typing import Callable
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.routing import APIRoute
import json


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


class HandlingErrorsRoute(APIRoute):
    """
    カスタム例外ハンドラ
    APIRouter単位のエラーハンドリング
    """

    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            if request.url.path.startswith("/handling-errors/case04/"):
                try:
                    return await original_route_handler(request)
                except StarletteHTTPException as exc:
                    return PlainTextResponse(
                        str(exc.detail), status_code=exc.status_code
                    )
                except RequestValidationError as exc:
                    return PlainTextResponse(str(exc), status_code=400)
            try:
                return await original_route_handler(request)
            except UnicornException as exc:
                return JSONResponse(
                    status_code=418,
                    content={
                        "message": f"Oops! {exc.name} did something. There goes a rainbow...",
                    },
                )

        return custom_route_handler


router = APIRouter(
    prefix="/handling-errors",
    tags=["エラーハンドリング"],
    route_class=HandlingErrorsRoute,
)

items = {"foo": "The Foo Wrestlers"}


@router.get("/case01/items/{item_id}")
async def read_item(item_id: str):
    """
    コード内でのHTTPExceptionの発生
    """
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )
    return {
        "item": items[item_id],
    }


@router.get("/case02/items-header/{item_id}")
async def read_item_header(item_id: str):
    """
    カスタムヘッダーの追加
    """
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={
                "X-Error": "There goes my error",
            },
        )
    return {
        "item": items[item_id],
    }


@router.get("/case03/unicorns/{name}")
async def read_unicorn(name: str):
    """
    カスタム例外ハンドラ
    """
    if name == "yolo":
        raise UnicornException(name=name)
    return {
        "unicorn_name": name,
    }


@router.get("/case04/items/{item_id}")
async def read_item(item_id: int):
    """
    デフォルトの例外ハンドラのオーバーライド
    """
    """
    # RequestValidationError
    curl -s -XGET \
        -H 'accept: application/json' \
        'http://127.0.0.1:8000/handling-errors/case04/items/xxx'
    # StarletteHTTPException
    curl -s -XGET \
        -H 'accept: application/json' \
        'http://127.0.0.1:8000/handling-errors/case04/items/3'
    """
    if item_id == 3:
        raise HTTPException(
            status_code=418,
            detail="Nope! I don't like 3.",
        )
    return {
        "item_id": item_id,
    }
