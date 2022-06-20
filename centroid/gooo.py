import cv2
import numpy as np

image = cv2.imread('ok.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
bbox = []
base = [212, 220, 383, 372]
# count = 0
db = []

for c in cnts:
    # Obtain bounding box coordinates and draw rectangleq
    x, y, w, h = cv2.boundingRect(c)
    bbox.append(x)
    bbox.append(y)
    bbox.append(w)
    bbox.append(h)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)


def check():
    count = 0
    if len(base) == len(bbox):
        print("START")
        if base[0] <= bbox[0] and base[0] >= base[0]:
            print("oK0")
            count += 1
        if base[1] <= bbox[1] and base[1] >= base[1]:
            print("oK1")
            count += 1
        if base[2] >= bbox[2]:
            print("oK2")
            count += 1
        if base[3] >= bbox[3]:
            print("oK3")
            count += 1

        if count == 4:
            db.append(1)
            print("Count is : {} ".format(count))
            print("Success")
            return True
        else:
            print("Count is : {} ".format(count))
            print("Error")
            return False
    else:
        print("ERROR")
        return "False & FIX"


print(check())

# cv2.imshow('image', image)
# cv2.waitKey()
