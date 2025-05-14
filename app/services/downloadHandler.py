import re
import os
import base64
import logging

import app.services.ExtractionOptions as EOps

from app.schemas.schema import VideoInfo, VideoResponse
from app.services.ThreadRV import ThreadWithReturnValue as TWRV



# IMAGE_PATH = f'thumbnail\\{os.listdir("thumbnail\\")[0]}'
THUMBNAIL_PATH = f'thumbnail\\'



def convert_image_to_base64():
    files = os.listdir(THUMBNAIL_PATH)
    try:
        with open(f"{THUMBNAIL_PATH}\\{files[0]}", "rb") as image_file:
            logging.info(f"Converting thumbnail to base64")
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    except Exception as e:
        logging.debug(f"Error converting image to base64: {str(e)}")
        return None
    finally:
        logging.info(f"Removing thumbnail")   
        os.remove(f"{THUMBNAIL_PATH}\\{files[0]}")




async def get_information(url,thumbnail_path = "thumbnail\\"):
    
    video_info = {}
    # regex pattern to extract required information
    pattern = r"'%\((\w+)\)s': ['\"](.*)['\"]"

    logging.info("Getting video quality")
    qualities_available = EOps.get_available_quality(url)
    EOps.getThumbnail(url, thumbnail_path)
    image_bytecode = convert_image_to_base64()
    
    logging.info("Extracting video information")
    t1 = TWRV(target=EOps.extract_video_info, args=(url,))
    t1.start()
    info = t1.join()
    
    for line in info.stdout:
        match = re.search(pattern, line.strip())
        if match:
            video_info[match.group(1)] = match.group(2)
        else:
            continue
    
    logging.info("Finalizing video information")
    video_info["thumbnail"] = image_bytecode
    ExtractedInfo = VideoInfo(**video_info)
    return VideoResponse(video_info=ExtractedInfo,available_resolutions=qualities_available)
            


def extract_download_info(line: str):
    pattern = re.compile(r"\[download\]\s+(?P<percentage>[\d.]+)%\s+of\s+(?P<size>[\d.]+\w+)\s+at\s+(?P<speed>[\d.]+\w+/s)\s+ETA\s+(?P<eta>\d{2}:\d{2})")
    match = pattern.search(line)
    if match:
        return match.groupdict()
    else:
        return None




