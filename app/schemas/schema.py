from typing import Optional, Set, Tuple
from pydantic import BaseModel, field_serializer, Field
import datetime

# create schemas 
class VideoInfo(BaseModel):
    title: Optional[str] = None
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
    @field_serializer("upload_date")
    def serialize_upload_date(upload_date: str):
        upload_date = datetime.datetime.strptime(upload_date, "%Y%m%d")
        return str(upload_date)


class VideoRequest(BaseModel):
    url: str


class VideoResponse(BaseModel):
    video_info: VideoInfo
    available_extensions: Set[str] = Field(default_factory=lambda: {"mp4","webm","mkv"})
    available_resolutions: Set[Tuple[str,str]]
    

class DownloadRequest(BaseModel):
    url: str
    quality: Optional[str]
    extension: Optional[str]