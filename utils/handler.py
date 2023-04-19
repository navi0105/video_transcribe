import os
import tempfile
import json
from typing import Optional

import pytube
import validators
from moviepy.editor import VideoFileClip

def extract_yt_audio(url: str,
                     temp: tempfile._TemporaryFileWrapper,
                     return_title: bool=True) -> Optional[str]:
    yt = pytube.YouTube(url)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download(filename=temp.name,
                   skip_existing=False)
    
    if return_title:
        return yt.title

def extract_audio(video_file: str, 
                  temp: tempfile._TemporaryFileWrapper):
    assert os.path.exists(video_file)
    print(f"Converting Video: {video_file}")

    video = VideoFileClip(video_file)
    video.audio.write_audiofile(temp.name)

def detect_type(file_or_url: str) -> str:
    # Audio
    if file_or_url.endswith('.mp3') or file_or_url.endswith('.wav'):
        assert os.path.exists(file_or_url)
        return 'audio'
    # Video
    elif file_or_url.endswith('.mp4'):
        assert os.path.exists(file_or_url)
        return 'video'
    
    # Just check if it is a valid url
    # cannot confirm it is YouTube video link
    if validators.url(file_or_url) == False:
        raise ValueError('input string is not .mp3/.wav/.mp4 file or valid url')

    return 'yt' 