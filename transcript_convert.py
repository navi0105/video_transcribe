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
        '--write-timestamp',
        action='store_true'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='transcript'
    )

    args = parser.parse_args()
    return args

def convert_transcript(file_path: str, output_dir: str, write_timestamp: bool=True) -> None:
    assert os.path.exists(file_path)
    print(f"Converting File: {file_path}")

    with open(file_path, 'r') as f:
        transcript = json.load(f)

    file_name = Path(file_path).stem
    with open(os.path.join(output_dir, f'{file_name}.txt'), 'w') as f:
        for segment in tqdm(transcript['segments'], total=len(transcript['segments'])):
            row = ""
            if write_timestamp:
                row += f"[{segment['start']} => {segment['end']}] "
            row += segment['text']

            f.write(row + '\n')

    print("Finished.")

def main():
    args = parse_args()

    Path(args.output_dir).mkdir(exist_ok=True, parents=True)

    for file_path in args.transcript_files:
        convert_transcript(file_path=file_path, 
                           output_dir=args.output_dir, 
                           write_timestamp=args.write_timestamp)

if __name__ == "__main__":
    main()