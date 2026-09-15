import logging
from importlib.metadata import version

from fastapi import FastAPI

from platform_services.api.health import router as health_router
from platform_services.config import Settings

settings = Settings()

logging.basicConfig(
    level=settings.log_level,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

app = FastAPI(title=settings.app_name, version=version("platform-services"))
app.include_router(health_router)
