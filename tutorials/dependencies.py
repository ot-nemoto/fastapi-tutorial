"""依存関係 - 最初のステップ
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/
"""

from typing import Union

from fastapi import APIRouter, Depends

from . import (
    classesAsDependencies,
    subDependencies,
    dependenciesInPathOperationDecorators,
    globalDependencies,
)

router = APIRouter(
    prefix="/dependencies",
    tags=["依存関係 - 最初のステップ"],
)

router.include_router(classesAsDependencies.router)
router.include_router(subDependencies.router)
router.include_router(dependenciesInPathOperationDecorators.router)
router.include_router(globalDependencies.router)


async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}


@router.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@router.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
