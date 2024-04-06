"""追加データ型
ref https://fastapi.tiangolo.com/ja/tutorial/extra-data-types/
"""

from datetime import datetime, time, timedelta
from typing import List, Union
from fastapi import APIRouter, Body, Path
from pydantic import BaseModel, Field
from uuid import UUID

router = APIRouter(
    prefix="/extra-data-types",
    tags=["追加データ型"],
)


@router.put("/items/{item_id}")
async def read_items(
    item_id: UUID,  # e.g. 6c84fb90-12c4-11e1-840d-7b25c5ee775a
    start_datetime: Union[datetime, None] = Body(default=None),
    end_datetime: Union[datetime, None] = Body(default=None),
    repeat_at: Union[time, None] = Body(default=None),
    process_after: Union[timedelta, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
