import whisper

# Load Whisper Model
model = whisper.load_model("base")

# Speech-to-Text Function
def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]