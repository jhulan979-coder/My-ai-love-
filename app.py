import gradio as gr
from gtts import gTTS
import os

# AI Companion ki personality (Hinglish tone)
SYSTEM_PROMPT = "You are a caring and loving AI friend. Talk in cute Hinglish."

def chat_and_speak(user_input):
    if not user_input or user_input.strip() == "":
        return None, "Kripya kuch boliye!"
    
    # Simple reply logic (Ise aap AI response se replace kar sakte hain)
    ai_reply = f"Aapne kaha: '{user_input}'. Mujhe aap se baat karke bohot accha lag raha hai! ❤️"
    
    # Voice generate karein (Hindi/Hinglish TTS)
    tts = gTTS(text=ai_reply, lang='hi', slow=False)
    audio_file = "voice.mp3"
    tts.save(audio_file)
    
    return audio_file, ai_reply

# Mobile-friendly Chat UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💖 My AI Companion")
    
    with gr.Row():
        # Companion Avatar Photo (Aap apni pasand ka link daal sakte hain)
        avatar = gr.Image(
            value="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
            label="AI Friend",
            interactive=False
        )
    
    audio_out = gr.Audio(label="Voice Reply", autoplay=True)
    text_out = gr.Textbox(label="AI Message", interactive=False)
    
    user_in = gr.Textbox(label="Aapka Message", placeholder="Yahan type karein...")
    btn = gr.Button("Send 💕", variant="primary")
    
    btn.click(fn=chat_and_speak, inputs=[user_in], outputs=[audio_out, text_out])

demo.launch()
