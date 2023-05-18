from enum import Enum, unique

from _types.service import Service


# service config
@unique
class ServiceEnums(Enum):
    """
    * `BUSINESS`: 业务服务
    * `DATA`: 数据服务
    """
    BUSINESS = Service(
        **{ "name": "business-01", "host": "127.0.0.1", "port": 50050 }
    )
    DATA = Service(**{ "name": "data-01", "host": "127.0.0.1", "port": 50051 })
