"""Request Files
ref https://fastapi.tiangolo.com/ja/tutorial/request-files/
"""

from typing import Annotated
from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/request-files",
    tags=["Request Files"],
)


@router.post("/case01/files/")
async def create_file(file: Annotated[bytes, File()]):
    """
    Define File Parameters
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "file=@README.md" \
        'http://127.0.0.1:8000/request-files/case01/files/' | jq .
    """
    return {
        "file_size": len(file),
    }


@router.post("/case01/uploadfile/")
async def create_upload_file(file: UploadFile):
    """
    File Parameters with UploadFile
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "file=@README.md" \
        'http://127.0.0.1:8000/request-files/case01/uploadfile/' | jq .
    """
    return {
        "filename": file.filename,
    }


@router.post("/case02/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    """
    Optional File Upload
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "file=" \
        'http://127.0.0.1:8000/request-files/case02/files/' | jq .
    """
    if not file:
        return {
            "message": "No file sent",
        }
    else:
        return {
            "file_size": len(file),
        }


@router.post("/case02/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    """
    Optional File Upload
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "file=" \
        'http://127.0.0.1:8000/request-files/case02/uploadfile/' | jq .
    """
    if not file:
        return {
            "message": "No upload file sent",
        }
    else:
        return {
            "filename": file.filename,
        }


@router.post("/case03/files/")
async def create_file(file: Annotated[bytes, File(description="A file read as bytes")]):
    """
    UploadFile with Additional Metadata
    """
    return {
        "file_size": len(file),
    }


@router.post("/case03/uploadfile/")
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    """
    UploadFile with Additional Metadata
    """
    return {
        "filename": file.filename,
    }


@router.post("/case04/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    """
    Multiple File Uploads
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "files=@README.md" \
        -F "files=@requirements.txt" \
        'http://127.0.0.1:8000/request-files/case04/files/' | jq .
    """
    return {
        "file_sizes": [len(file) for file in files],
    }


@router.post("/case04/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    """
    Multiple File Uploads
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F "files=@README.md" \
        -F "files=@requirements.txt" \
        'http://127.0.0.1:8000/request-files/case04/uploadfiles/' | jq .
    """
    return {
        "filenames": [file.filename for file in files],
    }


@router.post("/case05/files/")
async def create_files(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {
        "file_sizes": [len(file) for file in files],
    }


@router.post("/case05/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {
        "filenames": [file.filename for file in files],
    }
