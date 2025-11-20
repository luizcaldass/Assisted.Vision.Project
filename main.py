from CamWithYOLO import detect
from audioIA import speak
import time

def main():
    print("[INFO] Iniciando sistema de visão e áudio assistivo...")

    ultimo_objeto = None
    ultimo_tempo = 0
    intervalo_atualizacao = 0.5  # segundos entre atualizações

    try:
        while True:
            tempo_atual = time.time()

            if tempo_atual - ultimo_tempo > intervalo_atualizacao:
                objeto, confianca = detect()

                # Se o objeto mudou, atualiza a variável e fala
                if objeto != ultimo_objeto:
                    mensagem = f"Objeto {objeto} detectado à frente com {int(confianca * 100)}% de certeza."
                    speak(mensagem)
                    ultimo_objeto = objeto
                    ultimo_tempo = tempo_atual

            time.sleep(0.1)  # Pequeno delay para não sobrecarregar o sistema

    except KeyboardInterrupt:
        print("\n[INFO] Programa encerrado pelo usuário.")

if __name__ == "__main__":
    main()
