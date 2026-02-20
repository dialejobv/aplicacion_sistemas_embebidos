from gtts import gTTS
import os
import base64
import streamlit as st
import requests
from streamlit_mic_recorder import speech_to_text

# Configuración de DeepSeek
API_KEY = 'sk-2d5996dc3b04479e9dacbf5d0085ce60'  # Usa st.secrets en producción
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def enviar_mensaje(mensaje):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': 'deepseek-chat',
        'messages': [{'role': 'user', 'content': mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err.response.text}"
    except Exception as e:
        return f"Error inesperado: {str(e)}"

st.title("Tutor IA Voz")
st.write("Chatbot Habilitado por Voz - DeepSeek")

# Captura el texto de la voz del usuario
text = speech_to_text(language="es", use_container_width=True, just_once=True, key="STT")

if text:
    st.write("Tu:", text)
    
    # Obtener respuesta de DeepSeek
    respuesta = enviar_mensaje(text)
    
    # Convertir a voz
    tts = gTTS(respuesta, lang='es')
    tts.save("respuesta.mp3")

    # Reproducir audio
    with open("respuesta.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    st.audio(audio_bytes, format="audio/mp3")

    # Autoreproducción con JavaScript
    st.markdown(f"""
        <audio id="autoplay" autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        <script>
            document.getElementById('autoplay').play();
        </script>
    """, unsafe_allow_html=True)

    os.remove("respuesta.mp3")