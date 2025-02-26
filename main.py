import cv2
import mediapipe as mp

# Inicializacao dos modulos do mediapipe para detecçao das maos
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Inicia a captura de video com o opencv
cap = cv2.VideoCapture(0)

# Inicializacao do modelo de deteccao das maos
with mp_hands.Hands(
    model_complexity =0, # 0 é mais rapido enquanto 1 é mais preciso
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

# Verifica se a camera abriu ou nao
    if not cap.isOpened():
        print("Não foi possivel abrir a camera")
        exit()
    while cap.isOpened():
        ret, frame = cap.read()

# Verifica se o frame chegou ou nao
        if not ret:
            print("Não foi possivel receber o frame")
            continue

        frame.flags.writeable = False # Definido como falso para aumentar a performace
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Converte de BGR do opencv para RGB
        resultado = hands.process(frame) # Detecta as maos

# Desenha as landmarks da mao para cada mao
        frame.flags.writeable = True # Imagem volta a ser editavel
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # Retorna para o formato BGR
        if resultado.multi_hand_landmarks: # Se tiver alguma mão, então desenha as landmarks
            for hand_landmarks in resultado.multi_hand_landmarks: # Para cada mao que for detectada
                mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        cv2.imshow('Camera', cv2.flip(frame, 1)) # Mostra a camera espelhada
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()