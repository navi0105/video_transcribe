import argparse
import os
import tempfile
import json


import torch
import whisper
import pytube


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-u', '--url',
        type=str,
        required=True
    )
    parser.add_argument(
        '--model',
        type=str,
        default='large',
    )
    parser.add_argument(
        '--language',
        type=str,
        default='zh'
    )
    parser.add_argument(
        '--device',
        type=str,
        default='cuda'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='output.json'
    )
    

    args = parser.parse_args()
    return args

def get_video(url: str, temp: tempfile._TemporaryFileWrapper):
    video = pytube.YouTube(url)
    video.streams.filter().get_highest_resolution().download(filename=temp.name, skip_existing=True)

    return video

def get_transcript(model: whisper.Whisper, audio_file: str, language: str='zh') -> dict:
    assert os.path.exists(audio_file)
    print(f"Transcrbing Audio File: {audio_file}")
    
    transcript = model.transcribe(audio=audio_file, 
                                  language=language,
                                  initial_prompt="繁體中文")
    
    print("Finished.")

    return transcript

def main():
    args = parse_args()

    device = args.device

    if 'cuda' in device and torch.cuda.is_available() == False:
        device = 'cpu'

    model = whisper.load_model(name=args.model, device=device)
    temp = tempfile.NamedTemporaryFile(suffix='.mp3', delete=True)
    
    try:
        video = get_video(args.url, temp)
        transcript = get_transcript(model, temp.name, args.language)

        with open(args.output, 'w') as f:
            json.dump(transcript, f, indent=4, ensure_ascii=False)
    finally:
        temp.close()
  


if __name__ == "__main__":
    main()