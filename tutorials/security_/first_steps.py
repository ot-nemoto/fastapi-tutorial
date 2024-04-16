"""セキュリティ - 最初の一歩
ref https://fastapi.tiangolo.com/ja/tutorial/security/first-steps/
"""

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/first-steps",
    tags=["セキュリティ - 最初の一歩"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {
        "token": token,
    }
