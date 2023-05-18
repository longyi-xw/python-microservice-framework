from pathlib import Path

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.settings import settings
from core.consul import registerAll, deregisterAll
from enums.service import ServiceEnums
from api.api_v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


async def startup_event():
    registerAll(ServiceEnums.BUSINESS.value)


async def shutdown_event():
    deregisterAll(ServiceEnums.BUSINESS.value.name)


app.add_event_handler(event_type="startup", func=startup_event)
app.add_event_handler(event_type="shutdown", func=shutdown_event)
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", port=ServiceEnums.BUSINESS.value.port)
