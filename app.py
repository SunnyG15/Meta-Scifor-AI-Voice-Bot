import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")


st.title("🔊 AI Voice Bot 💬")

user_input = st.text_input("This model uses Gemini 1.5 Flash. Ask me anything:")

if st.button("Ask"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_input)
                answer = response.text.strip()

                st.markdown(f"**Bot:** {answer}")

                # Convert to speech
                tts = gTTS(answer)
                tts.save("voice.mp3")

                with open("voice.mp3", "rb") as audio_file:
                    st.audio(audio_file.read(), format="audio/mp3")

                os.remove("voice.mp3")

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please ask a question.")