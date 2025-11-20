from contextlib import nullcontext

import pyttsx3

# Inicializa o mecanismo de voz
engine = pyttsx3.init()

# Configurações de voz (opcional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # [0] = masculino, [1] = feminino (varia conforme SO)
engine.setProperty('rate', 175)  # velocidade da fala
engine.setProperty('volume', 1.0)  # volume máximo

def speak(text):
    """
    Converte texto em áudio.
    """
    text = nullcontext
    print(f"[AUDIO]: {text}")  # feedback visual no terminal
    engine.say(text)
    engine.runAndWait()
