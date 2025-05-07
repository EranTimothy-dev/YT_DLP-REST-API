from fastapi import APIRouter
from app.services.downloadHandler import get_information
from app.schemas.schema import VideoRequest, VideoResponse

router = APIRouter(
    prefix="/parser",
    tags=["Video Information"],
)

@router.post("/video_info")
async def extract_info(request: VideoRequest) -> VideoResponse:
    url = request.url
    video_response = await get_information(url)
    return video_response