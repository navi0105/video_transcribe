import os
import tempfile
from typing import Union

import streamlit as st
import whisper
import moviepy.editor as mp
import pytube

from module.whisper_model import TranscriptModel
from utils.handler import extract_audio
from transcript_to_srt import get_info

@st.cache_resource()
def load_transcript_model(model_name: str='base',
                       device: str='cuda:1'):
    model = TranscriptModel(model_name=model_name,
                            device=device)
    return model


def transcribe(temp_video: tempfile.NamedTemporaryFile,
                model: TranscriptModel) -> Union[str, dict]:
    if temp_video is not None:
        try:
            temp_audio = tempfile.NamedTemporaryFile(suffix='.mp3', delete=True)

            # Extract audio and transcribe
            extract_audio(video_file=temp_video.name,
                          temp=temp_audio)
            
            transcript = model.get_transcript(audio_file=temp_audio.name)
        finally:
            temp_audio.close()

        return transcript

def get_text(transcript: Union[str, dict],
             text_only: bool=False) -> str:
    if text_only:
        return transcript['text']
    
    return get_info(transcript['segments'])
    
    

def main():
    # Title
    st.title("Video/Audio Transcribe Tool")

    model = load_transcript_model('large')

    upload_type = st.radio(
        "Select upload type:",
        ("Local file", "YouTube url")
    )

    text_only = st.checkbox(label='Text Only')

    try:
        temp_video = tempfile.NamedTemporaryFile(suffix='.mp4', delete=True)
        if upload_type == 'Local file':
            file = st.file_uploader("Upload file", 
                                    accept_multiple_files=False,
                                    type=["mp4"])
            if file is not None:
                st.write("File name:", file.name)
                st.video(file)

                temp_video.write(file.getvalue())
        else:
            url = st.text_input("Enter YouTube URL")
            # Load YT Video to tempfile            
            
            # Download and display video
            if url:
                yt = pytube.YouTube(url)
                video = yt.streams.filter(file_extension='mp4').first()
                video.download(filename=temp_video.name)
                
                st.video(temp_video.name)

        if st.button('start transcribe.'):
            with st.spinner("Transcribing..."):
                transcript = transcribe(temp_video=temp_video, model=model)
                text = get_text(transcript=transcript, text_only=text_only)
            
            st.text_area(label='Transcript', 
                        value=text,
                        height=100)
    finally:
        temp_video.close()
        
        
        

if __name__ == "__main__":
    main()