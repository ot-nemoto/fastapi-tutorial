"""リクエストフォームとファイル
ref https://fastapi.tiangolo.com/ja/tutorial/request-forms-and-files/
"""

from fastapi import APIRouter, File, Form, UploadFile

router = APIRouter(
    prefix="/request-forms-and-files",
    tags=["リクエストフォームとファイル"],
)


@router.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    """
    ファイルとフォームフィールドがフォームデータとしてアップロード
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@README.md' \
        -F 'fileb=@requirements.txt' \
        -F 'token=xxxxx' \
        'http://127.0.0.1:8000/request-forms-and-files/files/' | jq .
    """
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }
