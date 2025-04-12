from fastapi import  FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(
    title="Youtube Downloader",
    description="An REST-API service for downloading youtube videos and audios",
    version="0.3.0",
    default_response_class=ORJSONResponse
    )






if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)