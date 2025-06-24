# speech.py

import os
import tempfile
import speech_recognition as sr
from gtts import gTTS
import streamlit as st

def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Please speak clearly.")
        audio = recognizer.listen(source, phrase_time_limit=10)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand your speech."
    except sr.RequestError:
        return "Could not connect to speech recognition service."

def speak_text(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)
        st.audio(tmp.name, format="audio/mp3")
