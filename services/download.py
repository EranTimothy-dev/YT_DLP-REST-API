import subprocess as sb
import threading
import time
import logging



THUMBNAIL_FILEPATH = "thumbnail/"
url1 = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
url = "https://youtu.be/whEObh8waxg?si=r6ggs4ZUjMy6hF7a"
video_download = ['yt-dlp', url,"-f", "bv*[height=720]+ba", "--merge-output-format", "mp4", "-P", "downloads\\", "-P", "temp:temp\\", "--windows-filenames"]

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('status.log')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
    

def download(cmd: list):
    process = sb.Popen(cmd, stdout=sb.PIPE, stderr=sb.STDOUT, text=True, universal_newlines=True, bufsize=1)
    # return process
    for line in process.stdout:
        logger.info(line)


    


# Process = download(video_download)
# get_download_data(Process)
# download(video_download)
t1 = threading.Thread(target=download, args=(video_download,))
t1.start()







