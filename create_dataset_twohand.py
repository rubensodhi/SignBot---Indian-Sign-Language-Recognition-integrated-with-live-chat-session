def db_twohand():
    import os
    import pickle
    from pathlib import Path
    import mediapipe as mp
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np


    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

    DATA_DIR = './data3'

    data = []
    labels = []
    for dir_ in os.listdir(DATA_DIR):
        for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
            data_aux = []

            x_ = []
            y_ = []

            img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = hands.process(img_rgb)


            if not (results.multi_hand_landmarks is None):
                    n = len(results.multi_hand_landmarks)
                    if n == 2:
                        try:
                            for hand_landmarks in results.multi_hand_landmarks:
                                 for i in range(len(hand_landmarks.landmark)):
                                      x= hand_landmarks.landmark[i].x
                                      y= hand_landmarks.landmark[i].y
                                      x_.append(x)
                                      y_.append(y)
                                 for i in range(len(hand_landmarks.landmark)):
                                       x = hand_landmarks.landmark[i].x
                                       y = hand_landmarks.landmark[i].y
                                       data_aux.append(x - min(x_))
                                       data_aux.append(y - min(y_))
                            data.append(data_aux)
                            labels.append(dir_)


                        except:
                                data_aux(np.zeros([1,189], dtype=int)[0])







    f = open('twohand.pickle', 'wb')
    pickle.dump({'data': data, 'labels': labels}, f)
    f.close()
