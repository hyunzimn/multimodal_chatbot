import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def query_groq_llm(image_caption, speech_text, model="llama3-8b-8192"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        f"이미지에는 이렇게 나와 있어: '{image_caption}'\n"
        f"그리고 사용자가 이렇게 말했어: '{speech_text}'\n"
        f"이 둘을 바탕으로 사용자에게 자연스럽고 친절하게 대답해줘."
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"요청 실패: {response.status_code}, {response.text}")
