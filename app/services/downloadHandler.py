import sys
import os
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
import app.services.DownloadOptions as VOps
import ExtractionOptions as EOps
import PlaylistOptions as PLOps
import LiveStreamOptions as LSOps
# from DownloadsPath import get_non_windows_download_folder, get_windows_download_folder
import base64


IMAGE_PATH = f'thumbnail_filepath\\{os.listdir("thumbnail\\")[0]}'


def convert_image_to_base64():
    try:
        with open(IMAGE_PATH, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    except Exception as e:
        print(f"Error converting image to base64: {str(e)}")
        return None




def get_information(url,thumbnail_path = "thumbnail\\"):
    qualities_available = list(EOps.get_available_quality(url)) 
    EOps.getThumbnail(url, thumbnail_path)
    image_bytecode = convert_image_to_base64()
    
    







