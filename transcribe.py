import os
import argparse
import json
from pathlib import Path

import torch
import whisper

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '--audio-files',
        nargs='+'
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
        '--output-dir',
        type=str,
        default='transcript'
    )
    

    args = parser.parse_args()
    return args


def get_transcript(model: whisper.Whisper, audio_file: str, language: str='zh') -> dict:
    assert os.path.exists(audio_file)
    print(f"Transcrbing Audio File: {audio_file}")
    
    transcript = model.transcribe(audio=audio_file, 
                                  language=language,)
    
    print("Finished.")

    return transcript

def main():
    args = parse_args()

    Path(args.output_dir).mkdir(exist_ok=True, parents=True)

    device = args.device

    if 'cuda' in device and torch.cuda.is_available() == False:
        device = 'cpu'

    model = whisper.load_model(name=args.model, device=device)

    for audio_path in args.audio_files:
        audio_name = Path(audio_path).stem
        transcript = get_transcript(model, audio_path, args.language)
        
        with open(os.path.join(args.output_dir, f'{audio_name}.json'), 'w') as f:
            json.dump(transcript, f, indent=4, ensure_ascii=False)
    

if __name__ == "__main__":
    main()
