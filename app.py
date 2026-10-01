import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="My AI Companion", page_icon="💖")

st.title("💖 My AI Companion")

# Companion Avatar Image
st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80", width=300)

user_input = st.text_input("Aapka Message:", placeholder="Yahan type karein...")

if st.button("Send 💕", type="primary"):
    if user_input.strip() != "":
        ai_reply = f"Aapne kaha: '{user_input}'. Mujhe aap se baat karke bohot accha lag raha hai! ❤️"
        
        # Audio generation
        tts = gTTS(text=ai_reply, lang='hi', slow=False)
        tts.save("voice.mp3")
        
        st.write("---")
        st.subheader("AI Message:")
        st.write(ai_reply)
        st.audio("voice.mp3", format="audio/mp3", autoplay=True)
    else:
        st.warning("Kripya kuch type karein!")
