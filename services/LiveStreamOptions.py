import subprocess




def download_live_stream(url):
    # cmd = ['yt-dlp',"--live-from-start","--cookies", "youtube.com_cookies.txt", url]
    cmd = ['yt-dlp',"--live-from-start","--cookies-from-browser", "firefox", url]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, text = True)