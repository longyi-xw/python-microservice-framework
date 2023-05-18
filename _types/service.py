from typing import Any, Optional

from pydantic import BaseModel


class Service(BaseModel):
    name: Optional[str]
    address: Optional[str]
    port: Optional[int]
    tags: Optional[list[str]]

    def __init__(self, name: str, host: str, port: int, tags=None, **data: Any):
        super().__init__(**data)
        if tags is None:
            tags = ["API"]
        self.name = name
        self.address = host
        self.port = port
        self.tags = tags
