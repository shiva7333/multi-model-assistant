# core/audio_engine.py
import whisper

# load a moderate whisper model; change "small" to "base"/"medium"/"large" if you have resources
_whisper = whisper.load_model("small")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe an audio file to text using Whisper.
    """
    res = _whisper.transcribe(file_path)
    return res.get("text", "")
