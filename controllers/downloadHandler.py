import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import services.DownloadOptions as dOpts
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



def get_video_information(url):
    qualities_available = list(dOpts.get_available_quality(url))
    dOpts.getThumbnail(url)
    image_bytecode = convert_image_to_base64()
    video_title,uploader,view_count,like_count = dOpts.get_video_info(url)
    return video_title,uploader,view_count,like_count,image_bytecode,qualities_available
    






