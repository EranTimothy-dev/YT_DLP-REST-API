from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class VideoInfo(BaseModel):
    id: Optional[UUID] = UUID
    title: str
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    view_count: Optional[str] = None
    like_count: Optional[str] = None
    duration: Optional[str] = None 
    available_resolutions: set


class VideoRequest(BaseModel):
    id: Optional[UUID] = UUID
    url: str