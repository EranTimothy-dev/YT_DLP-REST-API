from fastapi import  FastAPI
from fastapi.responses import ORJSONResponse
from typing import Optional
from subprocess import Popen

from app.schemas.schema import VideoRequest, VideoResponse, DownloadRequest
from app.services.ThreadRV import ThreadWithReturnValue
from app.services.downloadHandler import get_information
from app.services.DownloadOptions import download_video

app = FastAPI(
    title="Youtube Downloader",
    description="An REST-API service for downloading youtube videos and audios",
    version="0.3.0",
    default_response_class=ORJSONResponse
    )

download: Popen[str] = None
    
@app.post("/extract_video_info")
async def extract_info(request: VideoRequest) -> VideoResponse:
    url = request.url
    video_response = await get_information(url)
    return video_response
    

@app.post("/download_video")
async def download_yt_video(request: Optional[DownloadRequest]) -> dict:
    global download
    download = download_video(request.url, request.quality, request.extension)
    for line in download.stdout:
        print(f"\r{line.strip():<150}", end="",flush=True) # make sure the progress is printied on the same line
    print("\n Download Completed!")
    return {"ok": True}

@app.post("/stop_download")
async def stop_download():
    if isinstance(download,Popen[str]):
        download.terminate()
        print("\n Download Stopped!")
        return {"ok": True}
    elif download is None:
        return {"ok": False}
    

@app.post("/test")
async def test_endpoint(request: dict):
    return {"ok": True}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)