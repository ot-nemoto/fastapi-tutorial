"""レスポンスステータスコード
ref https://fastapi.tiangolo.com/ja/tutorial/response-status-code/
"""

from typing import Any, List, Union
from fastapi import APIRouter, status
from pydantic import BaseModel, EmailStr

router = APIRouter(
    prefix="/response-status-code",
    tags=["レスポンスステータスコード"],
)


@router.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {
        "status_code": name,
    }
