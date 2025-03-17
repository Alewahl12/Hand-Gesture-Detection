# Coletar as landmarks da mão de cada imagem
import os
import pickle
import cv2 as cv
import mediapipe as mp

# Configuração do mediapipe hands
mp_drawing = mp.solutions.drawing_utils #Desenha os pontos da mão
mp_hands = mp.solutions.hands #Modulo para detecção da mão
mp_drawing_styles = mp.solutions.drawing_styles #Estilo para desenhar os pontos da mão


hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3, model_complexity = 1) #Configuração da detecção das mãos
#static_image_mode serve para informar que estamos utilizando imagens fixas ao inves de video
#min_detection_confidence serve para dizer a confiança minima para dizer se é uma mão ou não, no caso é de 30% de confiança
#model_complexity serve para escolher um modelo de deteção mais complexo para melhores detecções, 0 é o padrão e 1 é mais complexo
#max_num_hands opcional para definir numero de mãos a serem detectadas

diretorio_dados = "./dados" #Pasta onde estão as subpastas com os diferentes simbolos com a mão
data = [] #Dados de cada gesto
labels =[] #Nome do gesto

for dir_ in os.listdir(diretorio_dados): #Lista todas as subpastas dentro da pasta dados
    for img_path in os.listdir(os.path.join(diretorio_dados, dir_)): #Para cada subpasta, iterar pelas imagens [:1] para processar uma imagem apenas para teste
        data_aux = []
        img = cv.imread(os.path.join(diretorio_dados, dir_, img_path)) #Carrega a imagem
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) #Converte a imagem do formato BGR(padrão do opencv) para RGB para processar com o mediapipe hands

        resultado = hands.process(img_rgb) # Processar a imagem

        if resultado.multi_hand_landmarks: # Se detectou alguma mão
            for hand_landmarks in resultado.multi_hand_landmarks: #Obter os pontos x e y das landmarks e salvar para cada imagem
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x) #salvar em um array
                    data_aux.append(y)#salvar em um array, o array representa nossa imagem

            data.append(data_aux) #Salva os dados coletados de cada imagem
            labels.append(dir_) #Salva o nome do gesto

#Salva os dados em um arquivo pickle com as labels respectivas
f = open('data.pickle', 'wb') 
pickle.dump({'data': data, 'labels': labels},f)
f.close()
