from fastapi import  FastAPI, Response, status, WebSocket, WebSocketDisconnect
from fastapi.responses import ORJSONResponse, HTMLResponse
from typing import Optional
from subprocess import Popen
from signal import SIGTERM
import signal
import asyncio
import psutil

from app.schemas.schema import VideoRequest, VideoResponse, DownloadRequest
from app.services.downloadHandler import get_information
from app.services.DownloadOptions import download_video

progress_queue = asyncio.Queue()

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
    
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global download
    await websocket.accept()
    try:
        while True:
            # if download is not None:
            message = await progress_queue.get()
            await websocket.send_text(f"{message}")
    except WebSocketDisconnect:
        print("Client disconnected")
    except asyncio.exceptions.CancelledError:
        print("Force Cancelled Client Connection")


loop = asyncio.get_event_loop()

@app.post("/download_video")
async def download_yt_video(request: Optional[DownloadRequest], response: Response) -> dict:
    global download
    

    def downloader():
        global loop
        global download
        download = download_video(request.url, request.quality, request.extension)
        for line in download.stdout:
            if download.returncode == SIGTERM:
                print("Stopping Download")
                try:
                    download.terminate()
                except RuntimeError:
                    print("Runtime error occurred")
                except Exception as e:
                    print(f"Error occurred: {str(e)}")
                return
            # asyncio.run(progress_queue.put(line))
            loop.call_soon_threadsafe(progress_queue.put_nowait, line)
            print(f"\r{line.strip():<150}", end="",flush=True) # make sure the progress is printied on the same line
        download.wait()

    await asyncio.to_thread(downloader)
    if download.returncode is None:
        response.status_code = status.HTTP_200_OK
        return {response.status_code: "Download completed!"}
    else:
        response.status_code = status.HTTP_409_CONFLICT
        return {response.status_code: "Client cancelled download!"}

@app.post("/stop_download")
async def stop_download(response: Response):
    global download
    # global loop
    if isinstance(download,Popen):
        try:
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
        # download.send_signal(signal.CTRL_BREAK_EVENT)
        # download.terminate()
        # download.kill()
        # loop.stop()
        print("\n Download Stopped!")
        return {response.status_code: "Download Stopped!"}
    elif download is None:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return {response.status_code: "No download runnning"}
    

@app.post("/test")
async def test_endpoint(request: dict):
    return {"ok": True}

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)