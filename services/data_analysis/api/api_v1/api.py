from fastapi import APIRouter
from .endpoints import index

api_router = APIRouter()
api_router.include_router(index.router, tags=["测试"])
