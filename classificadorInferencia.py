import cv2 as cv
import pickle
import numpy as np
import mediapipe as mp

#Carregar modelo com pickle
model_dict = pickle.load(open('./model.pickle', 'rb'))
model = model_dict['model']

#Escolher camera para capturar video
cap = cv.VideoCapture(0)

# Configuração do mediapipe hands
mp_drawing = mp.solutions.drawing_utils #Desenha os pontos da mão
mp_hands = mp.solutions.hands #Modulo para detecção da mão
mp_drawing_styles = mp.solutions.drawing_styles #Estilo para desenhar os pontos da mão

hands = mp_hands.Hands(static_image_mode = False, min_detection_confidence = 0.3, model_complexity = 1, max_num_hands = 1)

#Se a camera não abrir então deu erro
if not cap.isOpened():
    print("Erro ao acessar a câmera!")
    exit()

#Enquanto a camera estiver aberta, ler frame e exibir frame
while cap.isOpened():
    data_aux = []

    ret, frame = cap.read()

#Erro ao receber frame
    if not ret:
        print("Não foi possivel receber o frame")
        continue

    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB) #Converter cor para RGB

#Desenhar landmarks e connections da mão no frame
    resultado = hands.process(frame_rgb)
    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
#Obter os pontos x e y das landmarks
        for hand_landmarks in resultado.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x)
                data_aux.append(y)
        
        #Utilizar o predict para novos dados e mostrar o gesto feito
        predict = model.predict([np.asarray(data_aux)])
        print(predict)
    
#Mostra a camera espelhada(opcional) e fecha caso a tecla q seja pressionada
    cv.imshow('Camera',cv.flip(frame,1))
    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
