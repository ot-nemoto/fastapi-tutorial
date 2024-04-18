"""ミドルウェア
ref https://fastapi.tiangolo.com/ja/tutorial/middleware/
"""

import time

from fastapi import Request

import main


@main.app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    リクエストの処理とレスポンスの生成にかかった秒数を含むカスタムヘッダー X-Process-Time を追加
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
