from typing import Union
from fastapi import  FastAPI
from pydantic import BaseModel

app = FastAPI()

class VideoInfo(BaseModel):
    url: str
    title: str
    description: str | None = None
    thumbnail: str | None = None
    view_count: str | None = None
    like_count: str | None = None
    duration: str | None = None 
    available_resolutions: set


@app.get("/video")
def extract_video_information():
    pass