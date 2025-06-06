from modules.image_caption import imageCaption
from modules.speech_to_text import speech_to_text
from modules.ask_llm import query_groq_llm

def multimodal_chat(user_text, user_image_path, user_audio_path, api_key):
    context_parts = []

    if user_image_path:
        caption = imageCaption(user_image_path, api_key)
        context_parts.append(f"Image: {caption}")

    if user_audio_path:
        spoken_text = speech_to_text(user_audio_path, api_key)
        context_parts.append(f"Audio: {spoken_text}")

    if user_text.strip():
        context_parts.append(f"User typed: {user_text}")

    combined_prompt = "\n".join(context_parts) + "\nProvide a response:"
    response = query_groq_llm(combined_prompt, api_key)
    return response