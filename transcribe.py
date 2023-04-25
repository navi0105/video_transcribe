import os
import argparse
import json
import tempfile
from pathlib import Path
from tqdm import tqdm

import torch

from module.whisper_model import TranscriptModel
from utils.handler import extract_yt_audio, extract_audio, detect_type

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '-u', '--files-or-urls',
        nargs='+'
    )
    parser.add_argument(
        '--model',
        type=str,
        default='large',
    )
    parser.add_argument(
        '--text-only',
        type=bool,
        default=False,
    )
    parser.add_argument(
        '--device',
        type=str,
        default='cuda'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='transcript'
    )

    args = parser.parse_args()
    return args



def main():
    args = parse_args()

    Path(args.output_dir).mkdir(exist_ok=True, parents=True)

    device = args.device

    if 'cuda' in device and torch.cuda.is_available() == False:
        device = 'cpu'

    model = TranscriptModel(model_name=args.model,
                                       device=device)

    for file_or_url in tqdm(args.files_or_urls, total=len(args.files_or_urls)):
        try:
            use_temp = False
            data_type = detect_type(file_or_url=file_or_url)

            if data_type != 'yt':
                assert os.path.exists(file_or_url)

            audio_file = ''
            audio_name = ''
            if data_type == 'audio':
                audio_file = file_or_url
                audio_name = Path(audio_file).stem
            else:
                use_temp = True
                temp = tempfile.NamedTemporaryFile(suffix='.mp3', delete=True)
                audio_file = temp.name                
                # YouTube
                if data_type == 'yt':
                    url = file_or_url
                    audio_name = extract_yt_audio(url=url, 
                                             temp=temp,
                                             return_title=True)
                # Video
                else:
                    video_file = file_or_url
                    audio_name = Path(video_file).stem
                    extract_audio(video_file=video_file,
                                  temp=temp)   

            transcript = model.get_transcript(audio_file=audio_file, 
                                              text_only=args.text_only)                         
        finally:
            if use_temp:
                temp.close()
        
        ext = '.txt' if args.text_only else '.json'
        with open(os.path.join(args.output_dir, (audio_name + ext)), 'w') as f:
            if args.text_only:
                f.write(transcript)
            else:
                json.dump(transcript, f, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    main()
