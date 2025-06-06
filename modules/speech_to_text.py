import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def speech_to_text(audio_path, model="whisper-large-v3"):
    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    with open(audio_path, "rb") as f:
        audio_data = f.read()

    files = {
        "file": (audio_path, audio_data, "audio/wav")
    }

    data = {
        "model": model,
        "response_format": "json"
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        return response.json()["text"]
    else:
        raise Exception(f"요청 실패: {response.status_code}, {response.text}")


transcript = speech_to_text("your_audio.wav")
print("음성 텍스트:", transcript)