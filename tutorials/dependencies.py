"""依存関係 - 最初のステップ
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/
"""

from typing import Union

from fastapi import APIRouter, Depends

from .dependencies_ import (
    classes_as_dependencies,
    sub_dependencies,
    dependencies_in_path_operation_decorators,
    global_dependencies,
    dependencies_with_yield,
)

router = APIRouter(
    prefix="/dependencies",
    tags=["依存関係 - 最初のステップ"],
)

router.include_router(classes_as_dependencies.router)
router.include_router(sub_dependencies.router)
router.include_router(dependencies_in_path_operation_decorators.router)
router.include_router(global_dependencies.router)
router.include_router(dependencies_with_yield.router)


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
