import subprocess
import re
# import yt_dlp
import threading
import yt_dlp
# import pprint



playlist_url = "https://youtube.com/playlist?list=PLbpi6ZahtOH7c6nDA9YG3QcyRGbZ4xDFn&si=TClA3jkK99Ce2DRl"
thumbnail_filepath = "thumbnail\\"
url = "https://youtu.be/Js6H70-eADY?si=fF6a5sRPprlb1MDr"
age_restricted_video = "https://youtu.be/voQBX6yn2XY?si=e_4DHuE3jUDv5whc"


def get_video_info(url):
    # get the video information
    # Set up yt-dlp options
    ydl_opts = {
        'quiet': True,  # Suppress output
        'noplaylist': True,  # Do not download playlists
    }

    # Create a YoutubeDL instance with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract info from the URL
        info_dict = ydl.extract_info(url, download=False)  # Set download to False to only get metadata

        # Extract desired information
        video_title = info_dict.get('title', 'Unknown Title')
        uploader = info_dict.get('uploader', 'Unknown Uploader')
        view_count = info_dict.get('view_count', 'Unknown Views')
        like_count = info_dict.get('like_count', 'Unknown Likes')

        return video_title,uploader,view_count,like_count

        # Print the extracted information
        # print(f'Title: {video_title}')
        # print(f'Uploader: {uploader}')
        # print(f'Views: {view_count}')
        # print(f'Likes: {like_count}')

def get_available_quality(url):
    cmd = ['yt-dlp', url, "--list-formats", "--no-download"]
    output = subprocess.run(cmd, capture_output=True, text = True)
    pattern = r'\b(1080p|720p|480p|360p|240p|144p)\b'
    matches = re.findall(pattern, output.stdout.strip())
    return set(matches)


cmd = ['yt-dlp', url,"-f", "bv*[height=720]+ba"]
cmdDownloadAudio = ['yt-dlp', url,"-f", "ba"]

def download_live_stream(url):
    cmd = ['yt-dlp',"--live-from-start","--cookies", "youtube.com_cookies.txt", url]
    subprocess.run(cmd, text = True)


def getThumbnail(url):
    cmdThumbnail = ['yt-dlp', url, "--write-thumbnail", "--no-download","-P",thumbnail_filepath,"--windows-filenames"]
    subprocess.run(cmdThumbnail, capture_output=True, text = True)
    # print(output)

def download_playlist_selection(playlist_url:str, selection:str):
    cmd = ['yt-dlp',"-I", selection , playlist_url, "--yes-playlist", "-P", "playlist\\", "-P", "temp:temp\\","-f","bv*[height=720]+ba", "--merge-output-format", "mkv", "--windows-filenames"]
    subprocess.run(cmd, text = True)

def download_playlist_audio_selection(playlist_url:str, selection:str):
    cmd = ['yt-dlp', "-I", selection, playlist_url, "--yes-playlist", "--extract-audio", "--audio-format", "mp3"]
    subprocess.run(cmd, capture_output=True, text = True)

def download_playlist(playlist_url):
    cmd = ['yt-dlp', playlist_url, "--yes-playlist", "-P", "playlist\\", "-P", "temp:temp\\","-f","bv*[height=720]+ba", "--merge-output-format", "mkv", "--windows-filenames"]
    subprocess.run(cmd, text = True)

def download_playlist_audio(url):
    cmd = ['yt-dlp', playlist_url, "--yes-playlist", "--extract-audio", "--audio-format", "mp3"]
    subprocess.run(cmd, capture_output=True, text = True)

def download_audio(url):
    cmd = ['yt-dlp', url, "--extract-audio", "--audio-format", "mp3"]
    subprocess.run(cmd, capture_output=True, text = True)


def download_video(url,quality):
    cmd = ['yt-dlp', url,"-f", f"bv*[height={quality}]+ba","--merge-output-format", "mp4"]
    subprocess.run(cmd, text = True, check=True)








if __name__ == "__main__":
    youtubeLink = input("Enter the youtube link: ")
    print("download in progress...")
    t1 = threading.Thread(target=download_video, args=(youtubeLink,))
    t1.start()
    t1.join()
    # download_video(youtubeLink)
    # download_video(url)
    # download_playlist(playlist_url)
    print("download completed!")

    






