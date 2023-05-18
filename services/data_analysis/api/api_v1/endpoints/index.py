from fastapi import APIRouter
from enums.service import ServiceEnums
from enums.service_api import ServiceAPI
from utils.service_invoke import ConsulServiceUtil

router = APIRouter()


@router.get("/")
async def root():
    return { "message": "hello world 111" }


@router.get("/health", include_in_schema=False)
async def health():
    return { "message:"f" {ServiceEnums.DATA.value.name} ok!" }


@router.get("/hello/{name}")
async def say_hello(name: str):
    config = ServiceAPI.BUSINESS.value["say_hello"]
    config.params["name"] = name
    json = ConsulServiceUtil.call_service_method(ServiceEnums.BUSINESS.value.name, config)
    print(f"json response: {json}")
    return json
