import re
import os
import base64

from app.schemas.schema import VideoInfo, VideoResponse

import app.services.DownloadOptions as VOps
import app.services.ExtractionOptions as EOps
import app.services.PlaylistOptions as PLOps
import app.services.LiveStreamOptions as LSOps

from app.services.ThreadRV import ThreadWithReturnValue as TWRV

IMAGE_PATH = f'thumbnail\\{os.listdir("thumbnail\\")[0]}'
THUMBNAIL_PATH = f'thumbnail\\'




def convert_image_to_base64():
    try:
        with open(IMAGE_PATH, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    except Exception as e:
        print(f"Error converting image to base64: {str(e)}")
        return None




def get_information(url,thumbnail_path = "thumbnail\\"):
    
    video_info = {}
    qualities_available = EOps.get_available_quality(url)
    EOps.getThumbnail(url, thumbnail_path)
    image_bytecode = convert_image_to_base64()
    # regex pattern to extract required information
    pattern = r"'%\((\w+)\)s': ['\"](.*)['\"]"

    t1 = TWRV(target=EOps.extract_video_info, args=(url,))
    t1.start()
    info = t1.join()
    
    for line in info.stdout:
        match = re.search(pattern, line.strip())
        if match:
            video_info[match.group(1)] = match.group(2)
        else:
            continue

    video_info["thumbnail"] = image_bytecode
    ExtractedInfo = VideoInfo(**video_info)
    return VideoResponse(video_info=ExtractedInfo,available_resolutions=qualities_available)
            








