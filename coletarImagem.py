import cv2
import os

#Numero de fotos a capturar, intervalo em segundos, nome da pasta para salvar as imagens
def capturar_imagens(num_fotos, intervalo, pasta):
     
    # Inicializa a captura da webcam
    cap = cv2.VideoCapture(0)
    
    # Garante que a câmera foi aberta corretamente
    if not cap.isOpened():
        print("Erro ao acessar a câmera!")
        return


    image_save_path = f"dados\\{pasta}"

    os.makedirs(image_save_path, exist_ok=True)

    contador = 0  # Contador de fotos

    try:
        while contador < num_fotos:

            ret, frame = cap.read()  # Captura um frame da câmera

            if not ret:
                print("Erro ao capturar imagem!")
                break

            #Espelhamento da imagem e exibição
            cv2.imshow('Camera', cv2.flip(frame,1))


            # Salva a imagem
            nome_arquivo = f"foto_{contador}.jpg"
            cv2.imwrite(os.path.join(image_save_path, nome_arquivo),frame)
            print(f"Foto {contador} salva como {nome_arquivo}")

            contador += 1

            if cv2.waitKey(int(intervalo*1000)) == ord('q'):
                print("Captura interrompida pelo usuario")
                break

    finally:
        # Libera a câmera e fecha a janela
        cap.release()
        cv2.destroyAllWindows()
        print("Captura concluída!")

if __name__ == "__main__":
     capturar_imagens(100, 0.5, "1")
