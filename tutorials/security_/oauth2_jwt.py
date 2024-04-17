"""パスワード（およびハッシュ化）によるOAuth2、JWTトークンによるBearer
ref https://fastapi.tiangolo.com/ja/tutorial/security/oauth2-jwt/
"""

from datetime import datetime, timedelta, timezone
from typing import Union

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from tutorials.security_ import simple_oauth2

router = APIRouter(
    prefix="/oauth2-jwt",
    tags=["パスワード（およびハッシュ化）によるOAuth2、JWTトークンによるBearer"],
)

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(BaseModel):
    """
    レスポンスのトークンエンドポイントで使用するPydanticモデル
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


oauth2_scheme = simple_oauth2.oauth2_scheme
# security/simple-oauth2/token を有効にする場合は以下をコメントアウト
# ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="security/oauth2-jwt/token")


def verify_password(plain_password, hashed_password):
    """
    パスワードが保存されているハッシュと一致するかどうかを検証
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    パスワードをハッシュ化
    """
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db, username: str, password: str):
    """
    ユーザーを認証
    """
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    """
    新しいアクセストークンを生成
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    受け取ったJWTトークンを復号して検証しユーザを返す

    Parameters
    ----------
    token : str
        JWTトークン

    Returns
    -------
    user: UserInDB
        ユーザ

    Raises
    ------
    HTTPException
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    """
    アクティブユーザ（無効化されていないユーザ）を取得

    Raises
    ------
    HTTPException
    """
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Token:
    """
    有効期限を付きJWTアクセストークンを作成
    """
    """
    curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret=' \
        'http://127.0.0.1:8000/security/oauth2-jwt/token' | jq .
    """
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    カレントユーザを取得
    """
    """
    access_token=$(curl -s -XPOST \
        -H 'accept: application/json' \
        -H 'Content-Type: application/x-www-form-urlencoded' \
        -d 'grant_type=&username=johndoe&password=secret&scope=&client_id=&client_secret=' \
        'http://127.0.0.1:8000/security/oauth2-jwt/token' | jq -r '.access_token')
    curl -s -XGET \
        -H "accept: application/json" \
        -H "Authorization: Bearer ${access_token}" \
        'http://127.0.0.1:8000/security/oauth2-jwt/users/me/' | jq .
    """
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [
        {
            "item_id": "Foo",
            "owner": current_user.username,
        }
    ]
