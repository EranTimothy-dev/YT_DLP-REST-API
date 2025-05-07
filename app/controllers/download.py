from fastapi import Response, APIRouter, status
from fastapi.responses import ORJSONResponse
from typing import Optional
from subprocess import Popen
from signal import SIGTERM  
import asyncio
import psutil

from app.schemas.schema import DownloadRequest
from app.services.DownloadOptions import download_video, download_audio
from app.controllers.websocket import video_progress_queue, audio_progress_queue


router = APIRouter(
    prefix="/download",
    tags=["Video Download", "Audio Download"],
)

download: Popen[str] = None
loop = asyncio.get_event_loop()


@router.post("/video")
async def download_yt_video(request: Optional[DownloadRequest], response: Response) -> ORJSONResponse:
    global download

    def downloader():
        global loop
        global download
        download = download_video(request.url, request.quality, request.extension)
        for line in download.stdout:
            loop.call_soon_threadsafe(video_progress_queue.put_nowait, line)
            print(f"\r{line.strip():<150}", end="",flush=True) # make sure the progress is printied on the same line
        download.returncode = None

    # run sync function asynchronously as a thread
    await asyncio.to_thread(downloader)
    if download.returncode is None:
        response.status_code = status.HTTP_200_OK
        return {response.status_code: "Download completed!"}
    else:
        response.status_code = status.HTTP_409_CONFLICT
        return {response.status_code: "Client cancelled download!"}


@router.post("/audio")
async def download_yt_audio(request: Optional[DownloadRequest], response: Response) -> ORJSONResponse:
    global download
    def downloader():
        global loop
        global download
        download = download_audio(request.url)
        for line in download.stdout:
            loop.call_soon_threadsafe(audio_progress_queue.put_nowait, line)
            print(f"\r{line.strip():<150}", end="",flush=True) # make sure the progress is printied on the same line
        download.returncode = None

    await asyncio.to_thread(downloader)
    if download.returncode is None:
        response.status_code = status.HTTP_200_OK
        return {response.status_code: "Download completed!"}
    else:
        response.status_code = status.HTTP_409_CONFLICT
        return {response.status_code: "Client cancelled download!"}


@router.post("/stop")
async def stop_download(response: Response) -> ORJSONResponse:
    global download
    if isinstance(download,Popen):
        try:
            # terminate all process of download, created by ytdlp and ffmpeg
            parent = psutil.Process(download.pid)
            children = parent.children(recursive=True)
            for child in children:
                child.kill()
            parent.kill()
            print("Killed process and its children.")
        except Exception as e:
            print(f"Error killing process tree: {e}")
        response.status_code = status.HTTP_200_OK
        download.returncode = SIGTERM
        print("\n Download Stopped!")
        return {response.status_code: "Download Stopped!"}
    elif download is None:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {response.status_code: "No download runnning"}
