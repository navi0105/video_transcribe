import argparse
import os
import json
from tqdm import tqdm
from pathlib import Path
from typing import List


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '--transcript-files',
        nargs='+',
    )
    parser.add_argument(
        '-e', '--extension',
        type=str,
        default='.srt'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='transcript'
    )

    args = parser.parse_args()
    return args

def _get_timestring(timestamp: float):
    h = timestamp // 3600
    timestamp %= 3600
    m = timestamp // 60
    s = timestamp % 60
    ms = s - int(s)


    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(ms * 1000):03d}"

def convert_transcript(file_path: str, 
                       file_extension: str, 
                       output_dir: str) -> None:
    assert os.path.exists(file_path)
    print(f"Converting File: {file_path}")

    with open(file_path, 'r') as f:
        transcript = json.load(f)

    file_name = Path(file_path).stem
    with open(os.path.join(output_dir, (file_name + file_extension)), 'w') as f:
        for idx, segment in enumerate(tqdm(transcript['segments'], total=len(transcript['segments']))):
            info = ""

            start = _get_timestring(segment['start'])
            end = _get_timestring(segment['end'])

            info += f"{idx+1}\n"
            info += f"{start} --> {end}\n"
            info += segment['text']

            f.write(info + '\n\n')

    print("Finished.")

def main():
    args = parse_args()

    Path(args.output_dir).mkdir(exist_ok=True, parents=True)

    for file_path in args.transcript_files:
        convert_transcript(file_path=file_path,
                           file_extension=args.extension,
                           output_dir=args.output_dir)

if __name__ == "__main__":
    main()