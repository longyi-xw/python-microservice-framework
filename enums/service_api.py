from enum import Enum
from typing import Optional

from .service_verify import VerifyEnum


class RouteType:
    """
    :parameter

    * `api`: router path
    * `method`: GET | POST | PUT | DELETE
    * `params`: router params 注: 如果采用请求体传参要默认加上 `_is` 属性
    * `authentication_type`: 验证方式，1.微服务验证则只能进行服务之间数据交互 2.客户端验证
    * `alias`: 别名
    """
    api: str
    method: str
    params: Optional[dict]
    authentication_type: int
    alias: str
    response_model: Optional[object]

    def __init__(self, api: str, method: str, authentication_type: int, alias: str, params=None, response_model=None):
        self.api = api
        self.method = method
        self.authentication_type = authentication_type
        self.alias = alias
        self.params = params
        self.response_model = response_model


class ServiceAPI(Enum):
    """
    Routing for each microservice

    **Attributes**

    * `BUSINESS`: 业务服务
    * `DATA`: 数据服务
    """
    BUSINESS = {
        "root": RouteType(api="/", method="GET", authentication_type=VerifyEnum.MICROSERVICE.value, alias="根目录"),
        "say_hello": RouteType(api="/hello/{name}", method="GET", authentication_type=VerifyEnum.MICROSERVICE.value,
                               alias="输出测试信息", params={ "name": "" })
    }

    DATA = {

    }
