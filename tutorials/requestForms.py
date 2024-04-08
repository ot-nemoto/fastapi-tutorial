"""フォームデータ
ref https://fastapi.tiangolo.com/ja/tutorial/request-forms/
"""

from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/request-forms",
    tags=["フォームデータ"],
)


@router.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    """
    フォームを送信
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'username=nemoto' \
        -d 'password=password' \
        'http://127.0.0.1:8000/request-forms/login/' | jq .
    """
    return {
        "username": username,
    }
