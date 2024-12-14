import pickle
from time import sleep
import cv2
import sys
import mediapipe as mp
import ctypes
import chattt
from chattt import MedChat
from threading import Thread
import numpy as np
import os

model_dict1 = pickle.load(open('./model1.p', 'rb'))
model_dict2 = pickle.load(open('./model2.p', 'rb'))
model1 = model_dict1['model1']
model2 = model_dict2['model2']


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
string = '~'
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2 ,min_detection_confidence=0.3)
labels_dict1 = {0: '0', 1: '1', 2: '2',3: '3', 4: '4',5:'5',6: '6', 7: '7', 8: '8',9: '9', 10: 'C',11:'I',12: 'L', 13: 'O',14: 'U', 15: 'V'}
labels_dict2 = {0: 'A', 1: 'B', 2: 'D',3: 'E', 4: 'F',5:'G',6: 'H', 7: 'J', 8: 'K',9: 'M', 10: 'N',11:'P',12: 'Q', 13: 'R',14:'S',15: 'T', 16: 'W', 17: 'X',18: 'Y', 19: 'Z', 20: ' '}

#########################################
def _Detect():
    global string
    while True:
        if not string =='~':
            sleep(3)
            file = open('out.txt', 'a')
            file.write(string)
            file.close()
            print(string)
            string='~'

##########################################
#tp = Thread(target=_Detect)
def Inference_main():

    global string
    #tp.run()

    while True:

        data_aux = []
        x_ = []
        y_ = []

        ret, frame = cap.read()

        H, W, _ = frame.shape

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            n = len(results.multi_hand_landmarks)
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))
            if n == 1:

                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10

                x2 = int(max(x_) * W) - 10
                y2 = int(max(y_) * H) - 10

                prediction1 = model1.predict([np.asarray(data_aux)])

                predicted_character1 = labels_dict1[int(prediction1[0])]
                string = predicted_character1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character1, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                            cv2.LINE_AA)
            else:
                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10

                x2 = int(max(x_) * W) - 10
                y2 = int(max(y_) * H) - 10

                prediction2 = model2.predict([np.asarray(data_aux)])
                predicted_character2 = labels_dict2[int(prediction2[0])]
                string = predicted_character2
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character2, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                            cv2.LINE_AA)
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
        if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
            print("Yama")
            try:
                cap.release()
                cv2.destroyAllWindows()
                # Force exit all threads
                os._exit(0)  # This will force close all threads
            except:
                print(sys.exc_info()[0])

def Mediocer():
    try:
        p = Thread(target=Inference_main)
        p.daemon = True  # Make thread daemon so it exits when main program exits
        p.start()
        tp = Thread(target=_Detect)
        tp.daemon = True  # Make thread daemon so it exits when main program exits
        tp.start()
        MedChat()
    except:
        cap.release()
        cv2.destroyAllWindows()
        os._exit(0)
