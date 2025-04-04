from app.app_fastapi import app
from app.model.models import VideoInfo


@app.get("/video")
def extract_video_information():
    pass

