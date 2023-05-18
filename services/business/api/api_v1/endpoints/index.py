from fastapi import APIRouter, HTTPException, Depends

from core import security
from enums.service import ServiceEnums
from enums.service_api import ServiceAPI
from db.mongo import MongoDB_Wrapper
from services.business import models, crud
from ...deps import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)])
router.add_event_handler(event_type="shutdown", func=MongoDB_Wrapper.close)


@router.get(ServiceAPI.BUSINESS.value['root'].api)
async def root():
    return { "message": "hello world!" }


@router.get(ServiceAPI.BUSINESS.value['say_hello'].api)
async def say_hello(name: str):
    return { "message": f"hello {name}, I am {ServiceEnums.BUSINESS.value.name}" }


@router.post("/create_user", response_model=models.User)
async def create_user(user_in: models.User):
    user = crud.user.get(user_in.id)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user_in.password = security.get_password_hash(password=user_in.password)
    return crud.user.create(obj_in=user_in)


@router.get("/get_user/{id}", response_model=models.User)
async def get_user(object_id: str):
    user = crud.user.get(object_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="No user is queried. Procedure"
        )
    return user


@router.put("/update_user/{object_id}", response_model=models.User)
async def update_user(object_id: str, obj_in: models.User):
    user = crud.user.get(object_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="No user is queried. Procedure"
        )
    return crud.user.update(obj_in)


@router.delete("/del_user/{object_id}")
async def del_user(object_id):
    return crud.user.delete(object_id)


@router.get("/get_user_all/{page}/{page_size}", response_model=list[models.User])
async def get_user_all(page: int, page_size: int):
    # TODO: Multiple query parameters
    return crud.user.get_many(None, page, page_size)
