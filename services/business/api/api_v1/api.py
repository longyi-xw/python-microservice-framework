from fastapi import APIRouter
from .endpoints import index, login, check

api_router = APIRouter()
api_router.include_router(index.router, tags=["测试"])
api_router.include_router(login.router, tags=["认证"])
api_router.include_router(check.router)
