# Video transcribe Tool
Use `openai-whisper` tool to transcribe audio contents of video
## Environment
`python=3.9`
### Install Package
`pip install -r requirements.txt`

## Usage

### Transcribe from existed video file(s)
```bash
# Convert Video to audio
# You can input multiple video files at the same time
python video_convert.py \
    -f <video_file_1> <video_file_2> ... <video_file_n> \
    --output-dir <output_directory>

# Transcribe audio
# You can input multiple audio files at the same time
python transcribe.py \
    -f <audio_file_1> <audio_file_2> ... <audio_file_n> \
    --model <model_name> \
    --language <language> \
    --device <device> \
    --output-dir <output_dir>

# Extract text / time information from output transcript
# You can input multiple transcript files at the same time
python transcript_cextract.py \
    -f <transcript_file_1> <transcript_file_n> ... <transcript_file_n> \
    --write-timestamp \
    --output-dir <output_directory>
```

### Transcribe YouTube videos
```bash
# Transcribe Audio of YouTube Video
python transcribe_youtube.py \
    --url <youtube_url> \
    --model <model_name> \
    --language <language> \
    --device <device> \
    --output <output_transcription_file>
```

