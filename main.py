import os
from dotenv import load_dotenv
import gradio as gr
from modules.groq_inference import multimodal_chat

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def gradio_multimodal_interface(text_input, image_input, audio_input):
    return multimodal_chat(text_input, image_input, audio_input, GROQ_API_KEY)

with gr.Blocks() as demo:
    gr.Markdown("# Multimodal Chatbot using Groq + Gradio")
    text_box = gr.Textbox(label="Enter your text prompt")
    image_uploader = gr.Image(type="filepath", label="Upload an image (optional)")
    audio_recorder = gr.Audio(type="filepath", label="Record or upload audio (optional)")
    chat_button = gr.Button("Send")
    output_box = gr.Textbox(label="Chatbot Response")

    chat_button.click(
        fn=gradio_multimodal_interface,
        inputs=[text_box, image_uploader, audio_recorder],
        outputs=output_box
    )

if __name__ == "__main__":
    demo.launch()