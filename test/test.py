import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from services.DownloadOptions import getThumbnail

# SCRIPT_DIR = os.path.dirname(os.path.abspath('..'))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from services.DownloadOptions import getThumbnail
# from ..services.DownloadOptions import getThumbnail 
import threading

playlist_url = "https://youtube.com/playlist?list=PLbpi6ZahtOH7c6nDA9YG3QcyRGbZ4xDFn&si=TClA3jkK99Ce2DRl"
thumbnail_filepath = "thumbnail\\"
url = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
age_restricted_video = "https://youtu.be/voQBX6yn2XY?si=e_4DHuE3jUDv5whc"


getThumbnail(url)
# print(os.getcwd())



