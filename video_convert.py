import argparse
import os
from pathlib import Path

from moviepy.editor import VideoFileClip

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-f', '--video-files',
        nargs='+',
    )
    parser.add_argument(
        '--format',
        type=str,
        default='mp3'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='./audio'
    )

    args = parser.parse_args()
    return args

def convert_video(video_path: str, output_dir: str, format: str='mp3'):
    assert os.path.exists(video_path)
    print(f"Converting Video: {video_path}")
    video_name = Path(video_path).stem
    
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(os.path.join(output_dir, f"{video_name}.{format}"))
    print(f"Finished.")



def main():
    args = parse_args()

    # make output directory
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)

    for file_path in args.video_files:
        convert_video(video_path=file_path, output_dir=args.output_dir, format=args.format)

if __name__ == "__main__":
    main()