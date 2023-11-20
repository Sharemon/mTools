import cv2
import numpy as np

cap = cv2.VideoCapture(1)


cap.set(3, 2560)
cap.set(4, 720)
cap.set(15, -13)

while cap.isOpened():

    ret, frame = cap.read()

    if ret:
        left = frame[:, :1280]
        right = frame[:, 1280:]

        #cv2.imshow("left", left)
        cv2.imshow("right", right)
        key = cv2.waitKey(1)

        # gray = cv2.cvtColor(left, cv2.COLOR_RGB2GRAY)
        gray = cv2.cvtColor(right, cv2.COLOR_RGB2GRAY)

        lap = cv2.Laplacian(gray, cv2.CV_64F)
        img1 = cv2.convertScaleAbs(lap)

        print(np.sum(np.sum(img1, axis=1), axis=0))

        if key == 0x71:
            break