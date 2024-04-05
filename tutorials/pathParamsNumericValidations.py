"""パスパラメータと数値の検証
ref https://fastapi.tiangolo.com/ja/tutorial/path-params-numeric-validations/
"""

from typing import Annotated
from fastapi import APIRouter, Path, Query


router = APIRouter(
    prefix="/path-params-numeric-validations",
    tags=["パスパラメータと数値の検証"],
)


@router.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=0, le=1000)],
    q: str,
    size: float = Query(gt=0, lt=10.5),
):
    results = {
        "item_id": item_id,
    }
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results
