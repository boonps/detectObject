import cv2
import numpy as np
from cv2 import reduce

cap = cv2.VideoCapture("pk_lot.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)
vehicle_out = 0
vehicle_in = 0

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    # print(height, width)

    # roi = frame[300:600, 500:700]
    x, y, w, h = (242, 253, 1268, 699)
    roi = frame[y:y + h, x:x + w]
    # print(roi)
    cv2.rectangle(frame, (242, 253), (1268, 699), (0, 0, 255), 3)
    line = cv2.line(frame, (277, 424), (333, 256), (0, 255, 0), 2)
    cv2.line(frame, (985, 450), (959, 309), (0, 0, 255), 2)

    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    size = []

    for cnt in contours:

        area = cv2.contourArea(cnt)
        size.append(area)
        # sMax = max(size)

        if area > 1000:
            # print(max(size))
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
            xMid = int((x + (x + w)) / 2)
            yMid = int((y + (y + h)) / 2)
            pp = cv2.circle(roi, (xMid, yMid), 5, (255, 0, 0), 3)
            # print("center : {} {}".format(xMid, yMid))

            if xMid <= 30 + 20:
                vehicle_out += 1
                print("Count : {}\n".format(vehicle_out))
                cv2.line(frame, (277, 424), (333, 256), (255, 255, 255), 3)

            cv2.imshow("LOT", frame)
        cv2.putText(frame, "OUT: {}".format(vehicle_out), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255),
                    3)
        # cv2.imshow("Mark", mask)
        # cv2.imshow("ROI", roi)
        # print(vehicle_out)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
