from typing import Optional, Set
from pydantic import BaseModel, field_serializer
import datetime

# create schemas 
class VideoInfo(BaseModel):
    title: str
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    view_count: Optional[str] = None
    like_count: Optional[str] = None
    duration: Optional[str] = None 
    upload_date: Optional[str] = None
    uploader: Optional[str] = None
    @field_serializer("duration")
    def serialize_duration(duration: str):
        # serialize duration into hours, minutes and seconds
        time = int(duration)
        duration = datetime.timedelta(seconds=time)
        return str(duration)
        
    
    


class VideoRequest(BaseModel):
    url: str


class VideoResponse(BaseModel):
    video_info: VideoInfo
    available_extensions: Set = {"mp4","webm","mkv"}
    available_resolutions: Set
    