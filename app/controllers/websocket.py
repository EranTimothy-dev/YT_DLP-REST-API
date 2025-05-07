from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from typing import List
import asyncio
import logging

router = APIRouter(
    prefix="/ws",
    tags=["Websocket"],
)
logger = logging.getLogger(__name__)
video_progress_queue = asyncio.Queue()
audio_progress_queue = asyncio.Queue()
active_connections: List[WebSocket] = []

router.websocket("/video_download")
async def video_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("Client connected to video endpoint")
    active_connections.append(websocket)
    try:
        while True:
            message = await video_progress_queue.get()
            await websocket.send_text(f"{message}")
    except WebSocketDisconnect:
        logger.error("Client got disconnected from video endpoint")
    except asyncio.exceptions.CancelledError:
        logger.warning("Force Cancelled Client Connection")


@router.websocket("/audio_download")
async def audio_websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logger.info("Client connected to audio endpoint")
    active_connections.append(websocket)
    try:
        while True:
            message = await audio_progress_queue.get()
            await websocket.send_text(f"{message}")
    except WebSocketDisconnect:
        logger.error("Client got disconnected from audio endpoint")
    except asyncio.exceptions.CancelledError:
        logging.warning("Force Cancelled Client Connection")


@router.websocket("/disconnect")
async def disconnect():
    for websocket in active_connections:
        try:
            await websocket.close()
            active_connections.remove(websocket)
            logger.info("Client disconnected from all endpoints")
        except Exception as e:
            logger.error(f"Error disconnecting client: {str(e)}")

