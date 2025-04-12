from typing import Optional, Set
from pydantic import BaseModel

# create schemas 
class VideoInfo(BaseModel):
    title: str
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    view_count: Optional[str] = None
    like_count: Optional[str] = None
    duration: Optional[str] = None 
    


class VideoRequest(BaseModel):
    url: str


class VideoResponse(BaseModel):
    video_info: VideoInfo
    available_extensions: Set = {"mp4","webm","mkv"}
    available_resolutions: Set
    