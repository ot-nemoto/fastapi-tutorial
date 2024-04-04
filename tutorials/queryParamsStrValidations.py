"""クエリパラメータと文字列の検証
ref https://fastapi.tiangolo.com/ja/tutorial/query-params-str-validations/
"""

from typing import List, Union
from fastapi import APIRouter, Query


router = APIRouter(
    prefix="/query-params-str-validations",
    tags=["クエリパラメータと文字列の検証"],
)


# @router.get("/items/")
# async def read_items(q: List[str] = Query(default=[])):
#     query_items = {"q": q}
#     return query_items


@router.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        pattern="^[a-z]$",
        deprecated=True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
