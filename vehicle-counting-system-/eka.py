import cv2
import numpy as np

line_height = 1000  # 550

cap = cv2.VideoCapture('eka.png')

cv2.line(cap, (624, 914), (894, 918), (0, 255, 0), 2)

while (True):
    ret, frame = cap.read()
    # print(frame)
    cv2.imshow("Image", frame)
    # cv2.line(frame, (0, line_height), (1200, line_height), (0, 255, 0), 2)

    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break
cap.release()
cv2.destroyAllWindows()
