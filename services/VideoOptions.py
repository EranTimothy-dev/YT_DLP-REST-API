import subprocess



def download_audio(url):
    cmd = ['yt-dlp', url, "--extract-audio", "--audio-format", "mp3"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, capture_output=True, text = True)


def download_video(url):
    cmd = ['yt-dlp', url,"-f", f"bv*[height=720]+ba","--merge-output-format", "mp4", "-P", "downloads\\", "-P", "temp:temp\\","--windows-filenames","-N", "4"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, text = True, check=True)






