import pyttsx3

engine = pyttsx3.init()  # Inicializa o mecanismo de fala

# Configurações opcionais
engine.setProperty('rate', 170)   # velocidade da fala (padrão é ~200)
engine.setProperty('volume', 1.0) # volume máximo (0.0 a 1.0)

# Fala o texto
engine.say("Sistema de visão ativado. Testando saída de áudio.")
engine.runAndWait()
