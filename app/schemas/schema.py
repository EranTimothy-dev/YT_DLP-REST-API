from typing import Optional
from pydantic import BaseModel

# create schemas 
class VideoInfo(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    view_count: Optional[str] = None
    like_count: Optional[str] = None
    duration: Optional[str] = None 
    available_resolutions: set


class VideoRequest(BaseModel):
    id: Optional[int]
    url: str