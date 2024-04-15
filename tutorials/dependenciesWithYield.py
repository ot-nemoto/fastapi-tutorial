"""yieldを持つ依存関係
ref https://fastapi.tiangolo.com/ja/tutorial/dependencies/dependencies-with-yield/
"""

from fastapi import APIRouter
import sqlite3

router = APIRouter(
    prefix="/dependencies-with-yield",
    tags=["yieldを持つ依存関係"],
)

"""
I can't keep up with understanding.
"""
