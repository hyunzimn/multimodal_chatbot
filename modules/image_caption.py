import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def imageCaption(image_path):
  
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')


    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "이 이미지에 대해 설명해줘."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_data}"
                    }
                }
            ]
        }
    ]


    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": messages,
        "max_tokens": 100
    }


    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }


    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )


    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        raise Exception(f"요청 실패: {response.status_code}, {response.text}")


caption = generate_image_caption("your_image.png")
print("이미지 설명:", caption)