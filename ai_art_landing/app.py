import asyncio
import glob
import importlib
import os
import shutil
import sys

from pathlib import Path

from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from utils.logger import log_server_info
from contextlib import asynccontextmanager
from ai_art_landing.settings import settings
from .core import init_core_routers


async def startup(app: FastAPI):
    settings.app_running = True

    log_server_info()

    # register core routes
    init_core_routers(app)


async def shutdown():
    logger.warning("APP shutting down...")
    settings.app_running = False

    # wait a bit to allow them to finish, so that cleanup can run without problems
    await asyncio.sleep(0.1)

    # but nothing to do


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup(app)
    yield
    await shutdown()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_title,
        description=(
            "API for AI Art, the path to financial liberty"
        ),
        version=settings.version,
        lifespan=lifespan,
        license_info={
            "name": "MIT License",
        },
    )

    # register static files
    static_path = Path("ai_art_landing", "static")
    static = StaticFiles(directory=static_path)
    app.mount("/static", static, name="static")

    return app
