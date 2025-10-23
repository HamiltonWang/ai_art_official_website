from fastapi import APIRouter, FastAPI

from ai_art_landing.core.generic import generic_router

core_app = APIRouter(tags=["Core"])


def init_core_routers(app: FastAPI):
    app.include_router(core_app)
    app.include_router(generic_router)

