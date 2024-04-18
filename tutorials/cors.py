"""CORS (オリジン間リソース共有)
ref https://fastapi.tiangolo.com/ja/tutorial/cors/
"""

from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

import main

router = APIRouter(
    prefix="/cors",
    tags=["CORS (オリジン間リソース共有)"],
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

main.app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get("/")
async def main():
    """
    Sample
    """
    """
    curl -s -XOPTIONS \
        -H 'accept: application/json' \
        -H 'Access-Control-Request-Method: POST' \
        -H 'Origin: http://localhost' \
        'http://127.0.0.1:8000/cors/'
    """
    """
    curl -s -XGET \
        -H 'accept: application/json' \
        'http://127.0.0.1:8000/cors/' | jq .
    """
    return {
        "message": "Hello World",
    }
