from fastapi import FastAPI
from app.controllers.download import router as download_router
from app.controllers.info_parser import router as info_parser_router
from app.controllers.websocket import router as websocket_router


def register_routes(app: FastAPI) -> None:
    app.include_router(download_router)
    app.include_router(info_parser_router)
    app.include_router(websocket_router)