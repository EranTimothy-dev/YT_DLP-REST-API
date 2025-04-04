from typing import Optional
from pydantic import BaseModel

class VideoInfo(BaseModel):
    url: str
    title: str
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    view_count: Optional[str] = None
    like_count: Optional[str] = None
    duration: Optional[str] = None 
    available_resolutions: set