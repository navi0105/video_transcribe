import whisper
from typing import Union, Optional

class TranscriptModel:
    def __init__(self,
                 model_name: str,
                 device: str='cuda'):
        self.model = whisper.load_model(model_name, device=device)

    def _detect_language(self, 
                         audio_file: str) -> str:
        audio = whisper.load_audio(audio_file)
        audio = whisper.pad_or_trim(audio)

        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)

        _, probs = self.model.detect_language(mel)

        return max(probs, key=probs.get)

    def get_transcript(self,
                       audio_file: str,
                       text_only: bool=False) -> Union[str, dict]:
        print(f"Transcribing Audio File: {audio_file}")

        language = self._detect_language(audio_file)
        transcript = self.model.transcribe(audio=audio_file,
                                           language=language)

        if text_only == True:
            return transcript['text']

        print("Done.")
        return transcript
