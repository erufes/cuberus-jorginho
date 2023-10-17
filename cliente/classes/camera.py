import select
import cv2
import os

class camera():
    def __init__(self):
        self.frame = None
    
    # Função para tirar uma foto com o nome face1.jpg a face6.jpg
    def tirar_foto(self):
        for num in range(1, 7):
            nome_arquivo = f"fotos/face{num}.png"
            if os.path.exists(nome_arquivo):
                continue

            # Salvar o frame como uma imagem
            cv2.imwrite(nome_arquivo, self.frame)
            print(f"Foto tirada e salva como '{nome_arquivo}'.")
            break

    def video(self):    
        # Inicialize a captura de vídeo a partir da câmera USB
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # 0 refere-se à primeira câmera, 1 seria a segunda, e assim por diante

        # Verifique se a captura de vídeo foi inicializada corretamente
        if not cap.isOpened():
            print("Erro: Não foi possível abrir a câmera.")
            exit()

        # Loop para capturar e exibir os frames da câmera
        while True:
            ret, self.frame = cap.read()  # Captura um frame da câmera

            if not ret:
                print("Erro: Não foi possível capturar o frame.")
                break

            # Exibe o frame em uma janela
            cv2.imshow('Camera cubo', self.frame)

            # Verifique se a tecla 'q' foi pressionada para sair do loop
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                break

        # Libere os recursos e feche a janela
        cap.release()
        cv2.destroyAllWindows()