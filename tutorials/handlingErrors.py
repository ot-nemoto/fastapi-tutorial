"""エラーハンドリング
ref https://fastapi.tiangolo.com/ja/tutorial/handling-errors/
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import main

router = APIRouter(
    prefix="/handling-errors",
    tags=["エラーハンドリング"],
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


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@main.app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """
    カスタム例外ハンドラ
    """
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. There goes a rainbow...",
        },
    )


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


# @main.app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     """
#     デフォルトの例外ハンドラのオーバーライド
#     """
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @main.app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     """
#     デフォルトの例外ハンドラのオーバーライド
#     """
#     return PlainTextResponse(str(exc), status_code=400)
#
#
# @router.get("/case04/items/{item_id}")
# async def read_item(item_id: int):
#     """
#     デフォルトの例外ハンドラのオーバーライド
#     """
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {
#         "item_id": item_id,
#     }
