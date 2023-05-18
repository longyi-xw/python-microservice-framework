import secrets
from functools import lru_cache
from os.path import dirname, abspath

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    project settings
    """

    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # expirationTime (60 minutes * 24 hours * 8 days = 8 days)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: list[str]

    # mongodb
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_HOST: str
    MONGO_INITDB_DATABASE: str

    class Config:
        env_file = f"{dirname(dirname(abspath(__file__)))}/.env"
        case_sensitive = True


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
