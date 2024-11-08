import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import services.DownloadOptions as d
import base64

IMAGE_PATH = 'thumbnail_filepath\\'


def convert_image_to_base64():
    try:
        with open(IMAGE_PATH, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    except Exception as e:
        print(f"Error converting image to base64: {str(e)}")
        return None



def get_video_information(url):
    qualities_available = list(d.get_available_quality(url))
    d.getThumbnail(url)
    






