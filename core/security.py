from datetime import timedelta, datetime
from typing import Union, Any

import jwt
from passlib.context import CryptContext

from config.settings import settings

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """
    Token Generator
    :param subject:
    :param expires_delta:
    :return:
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = { "exp": expire, "sub": str(subject) }
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)

    # TODO: Storage database
    return encode_jwt


def verity_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
