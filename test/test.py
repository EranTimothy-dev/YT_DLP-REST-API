import threading
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from services.DownloadOptions import getThumbnail, download_video

# SCRIPT_DIR = os.path.dirname(os.path.abspath('..'))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
# from services.DownloadOptions import getThumbnail
# from ..services.DownloadOptions import getThumbnail 
import threading

playlist_url = "https://youtube.com/playlist?list=PLbpi6ZahtOH7c6nDA9YG3QcyRGbZ4xDFn&si=TClA3jkK99Ce2DRl"
thumbnail_filepath = "thumbnail\\"
url = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
url1 = "https://youtu.be/whEObh8waxg?si=kBbfH05WMNQpNTvJ"
age_restricted_video = "https://youtu.be/voQBX6yn2XY?si=e_4DHuE3jUDv5whc"


# getThumbnail(url)
# print(os.getcwd())
# files = os.listdir(thumbnail_filepath)
# print(files[0])
# process = download_video(url1)
# for line in process.stdout:
#     print(line.strip())

# make a thread class with return value
class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, *, daemon=None,
                 verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return


t1 = ThreadWithReturnValue(target=download_video, args=(url1,))
t1.start()
process = t1.join()
for line in process.stdout:
    print(line.strip())



