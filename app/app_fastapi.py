from fastapi import  FastAPI
from fastapi.responses import ORJSONResponse

from app.schemas.schema import VideoRequest

from app.services.downloadHandler import get_information

app = FastAPI(
    title="Youtube Downloader",
    description="An REST-API service for downloading youtube videos and audios",
    version="0.3.0",
    default_response_class=ORJSONResponse
    )

    
@app.post("/extract_video_info")
async def extract_info(request: VideoRequest):
    url = request.url
    video_response = await get_information(url)
    return video_response
    

@app.post("/test")
async def test_endpoint(request: dict):
    return {"ok": True}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)