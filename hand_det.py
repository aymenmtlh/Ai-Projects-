import cv2 
import pyfirmata
import mediapipe as mp 
import numpy as np 


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils 
hands = mp_hands.Hands(min_detection_confidence=0.8)
ws , hs = 1280 , 720 

cap = cv2.VideoCapture(0)
cap.set(3 ,ws )
cap.set(4,hs)
#board = pyfirmata.Arduino('COM3')
#servo_pinX = board.get_pin('d:9:s')

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    
    
    #hand detection 
    multiHandDetection =  results.multi_hand_landmarks

    lmList =[]
    if multiHandDetection:
        #Hand Visualization
        for id, lm in enumerate(multiHandDetection):
            mp_draw.draw_landmarks(img, lm, mp_hands.HAND_CONNECTIONS,
                                  mp_draw.DrawingSpec(color=(0, 255,255), thickness=4, circle_radius=7),
                                  mp_draw.DrawingSpec(color=(0, 0, 0), thickness = 4))
         #Hand Tracking
        singleHandDetection = multiHandDetection[0]
        for lm in singleHandDetection.landmark:
            h, w, c = img.shape
            lm_x, lm_y = int(lm.x*w), int(lm.y*h)
            lmList.append([lm_x, lm_y])
        print(lmList)
        # draw point
        myLP = lmList[8]
        px, py = myLP[0], myLP[1]
        cv2.circle(img, (px, py), 15, (255, 0, 255), cv2.FILLED)
        cv2.putText(img, str((px, py)), (px + 10, py - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
        cv2.line(img, (0, py), (ws, py), (0, 0, 0), 2)  # x line
        cv2.line(img, (px, hs), (px, 0), (0, 0, 0), 2)  # y line

        # convert position to degree value
        #servoX = int(np.interp(px, [0, ws], [180, 0]))
        ##servoY = int(np.interp(py, [0, hs], [0, 180]))
        #cv2.rectangle(img, (40, 20), (350, 110), (0, 255, 255), cv2.FILLED)
        #cv2.putText(img, f'Servo X: {servoX} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        ##cv2.putText(img, f'Servo Y: {servoY} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
#
        #servo_pinX.write(servoX)
        ##servo_pinY.write(servoY)

        print(f'Hand Position x: {px} y: {py}')
        #print(f'Servo Value x: {servoX} y: {servoY}'

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()