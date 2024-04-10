"""エラーハンドリング
ref https://fastapi.tiangolo.com/ja/tutorial/handling-errors/
"""

from typing import Callable

from fastapi import APIRouter, HTTPException, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.routing import APIRoute
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException

import main


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
            if request.url.path.startswith("/handling-errors/case05/"):
                try:
                    return await original_route_handler(request)
                except RequestValidationError as exc:
                    return JSONResponse(
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=jsonable_encoder(
                            {"detail": exc.errors(), "body": exc.body}
                        ),
                    )
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


# @main.app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={
#             "message": f"Oops! {exc.name} did something. There goes a rainbow...",
#         },
#     )


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
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# @main.app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)


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


# @main.app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder(
#             {
#                 "detail": exc.errors(),
#                 "body": exc.body,
#             }
#         ),
#     )


class Item(BaseModel):
    title: str
    size: int


@router.post("/case05/items/")
async def create_item(item: Item):
    """
    RequestValidationErrorのボディを使用
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
            "title": "towel",
            "size": "XL"
        }' \
        'http://127.0.0.1:8000/handling-errors/case05/items/' | jq .
    """
    return item


# @main.app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     """
#     FastAPI の例外ハンドラの再利用
#     """
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)
#
#
# @main.app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     """
#     FastAPI の例外ハンドラの再利用
#     """
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)
#
