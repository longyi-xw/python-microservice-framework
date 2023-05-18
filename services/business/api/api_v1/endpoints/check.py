from fastapi import APIRouter

from enums.service import ServiceEnums

router = APIRouter()


@router.get("/health", include_in_schema=False)
async def health():
    return { "message:" f" {ServiceEnums.BUSINESS.value.name} ok!" }
