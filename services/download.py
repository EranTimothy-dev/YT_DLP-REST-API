import subprocess as sb
import yt_dlp
import re
import base64
import threading
import time
# import asyncio

THUMBNAIL_FILEPATH = "thumbnail/"
url1 = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
url = "https://youtu.be/whEObh8waxg?si=r6ggs4ZUjMy6hF7a"
video_download = ['yt-dlp', url,"-f", "bv*[height=720]+ba", "--merge-output-format", "mp4", "-P", "downloads\\", "-P", "temp:temp\\", "--windows-filenames"]




    

def download(cmd: list):
    process = sb.Popen(cmd, stdout=sb.PIPE, stderr=sb.STDOUT, text=True, universal_newlines=True, bufsize=1)
    # return process
    with open("download_status.txt","a") as file:
        for line in process.stdout:
            file.write(line.strip()+ '\n')



    


# Process = download(video_download)
# get_download_data(Process)
# The line `Process = download(video_download)` is calling the `download` function with the
# `video_download` list as an argument and assigning the result to the variable `Process`. The
# `download` function initiates a subprocess to download a video using the specified command list,
# captures the download progress, and prints the progress, speed, ETA, and download size information
# as the video is being downloaded.
# download(video_download)
t1 = threading.Thread(target=download, args=(video_download,))
# t2 = threading.Thread(target=read_from_file)

t1.start()
time.sleep(4)
# t2.start()

# t1.join()
# t2.join()







