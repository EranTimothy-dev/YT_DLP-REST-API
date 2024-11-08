import subprocess
import os
# from pathlib import Path
from packages.DownloadsPath import get_windows_download_folder, get_non_windows_download_folder



def merge_codecs(video_file,audio_file,output_file):
    '''
    Merges a video file with an audio file into a single output file.

    Args:
        video_file (str): Path to the video file to be merged.
        audio_file (str): Path to the audio file to be merged.
        output_file (str): Desired path and name for the output file.

    Requirements:
        - FFmpeg must be installed and added to the system PATH.
        - `ffmpeg.exe` should be in the current working directory for this function to run without errors.

    Behavior:
        - Merges the video and audio files using FFmpeg with the "copy" codec.
        - Saves the merged file to the Downloads folder.
        - Deletes the original video and audio files if they exist.
        - Deletes the "videos" directory in the current working directory if it exists.

    Note:
        The function determines the Downloads folder based on the operating system:
        - For Windows, it uses `get_windows_download_folder`.
        - For non-Windows systems, it uses `get_non_windows_download_folder`.

    Raises:
        FileNotFoundError: If the specified video or audio files do not exist.

    Example:
        merge_codecs("path/to/video.mp4", "path/to/audio.mp3", "output.mp4")
    '''
    if os.name == "nt":
        path = get_windows_download_folder()
    else:
        path = get_non_windows_download_folder()
    
    output = path + "\\" + fr"{output_file}"
    codec = "copy"
    subprocess.run(f"ffmpeg -y -i {video_file} -i {audio_file} -c {codec} {output}")
    print("Video and Audio files merged successfully.")

    if os.path.exists(video_file) and os.path.exists(audio_file):
        os.remove(video_file)
        os.remove(audio_file)
        # os.rmdir(path+"\\videos")
        os.rmdir("videos")
        print("Unnecessary files deleted successfully.")
    else:
        print("file not found")
    
    