"""依存関係としてのクラス
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/classes-as-dependencies/
"""

from typing import Union

from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/classes-as-dependencies",
    tags=["依存関係としてのクラス"],
)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@router.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
