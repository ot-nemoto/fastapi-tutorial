"""Simple OAuth2 with Password and Bearer
ref https://fastapi.tiangolo.com/ja/tutorial/security/simple-oauth2/
"""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter(
    prefix="/simple-oauth2",
    tags=["Simple OAuth2 with Password and Bearer"],
)

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="security/simple-oauth2/token")


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(
            status_code=400,
            detail="Inactive user",
        )
    return current_user


@router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    アクセストークンを作成
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret=' \
        'http://127.0.0.1:8000/security/simple-oauth2/token' | jq .
    """
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password",
        )

    return {
        "access_token": user.username,
        "token_type": "bearer",
    }


@router.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """
    カレントユーザを取得
    """
    """
    access_token=$(curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret=' \
        'http://127.0.0.1:8000/security/simple-oauth2/token' | jq -r '.access_token')
    curl -s -XGET \
        -H "accept: application/json" \
        -H "Authorization: Bearer ${access_token}" \
        'http://127.0.0.1:8000/security/simple-oauth2/users/me' | jq .
    """
    return current_user
