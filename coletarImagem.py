#Coletar imagens dos gestos
import cv2 as cv
import os

#Numero de fotos a capturar, intervalo em segundos, nome da pasta para salvar as imagens
def capturar_imagens(num_fotos, intervalo, pasta):
     
    # Inicializa a captura da webcam
    cap = cv.VideoCapture(0)
    
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
            cv.imshow('Camera', cv.flip(frame,1))


            # Salva a imagem
            nome_arquivo = f"foto_{contador}.jpg"
            cv.imwrite(os.path.join(image_save_path, nome_arquivo),frame)
            print(f"Foto {contador} salva como {nome_arquivo}")

            contador += 1

            if cv.waitKey(int(intervalo*1000)) == ord('q'): # Aguarda o intervalo para tirar foto ou encerra a captura caso pressione q
                print("Captura interrompida pelo usuario")
                break

    finally:
        # Libera a câmera e fecha a janela
        cap.release()
        cv.destroyAllWindows()
        print("Captura concluída!")

if __name__ == "__main__":
     capturar_imagens(100, 0.2, "3") #Escolher numero de fotos e intervalo entre cada captura
