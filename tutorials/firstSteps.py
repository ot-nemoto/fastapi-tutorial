"""最初のステップ
ref https://fastapi.tiangolo.com/ja/tutorial/first-steps/
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/first-steps",
    tags=["最初のステップ"],
)


@router.get("/")
async def root():
    return {"message": "Hello World"}
