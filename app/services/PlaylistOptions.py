import subprocess



def download_playlist_selection(playlist_url:str, selection:str):
    cmd = ['yt-dlp',"-I", selection , playlist_url, "--yes-playlist", "-P", "playlist\\", "-P", "temp:temp\\","-f","bv*[height=720]+ba", "--merge-output-format", "mkv", "--windows-filenames"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, text = True)

def download_playlist_audio_selection(playlist_url:str, selection:str):
    cmd = ['yt-dlp', "-I", selection, playlist_url, "--yes-playlist", "--extract-audio", "--audio-format", "mp3"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, capture_output=True, text = True)

def download_playlist(playlist_url):
    cmd = ['yt-dlp', playlist_url, "--yes-playlist", "-P", "playlist\\", "-P", "temp:temp\\","-f","bv*[height=720]+ba", "--merge-output-format", "mkv", "--windows-filenames"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, text = True)

def download_playlist_audio(playlist_url):
    cmd = ['yt-dlp', playlist_url, "--yes-playlist", "--extract-audio", "--audio-format", "mp3"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, universal_newlines=True, bufsize=1)
    return process
    # subprocess.run(cmd, capture_output=True, text = True)






