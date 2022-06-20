import cv2
import numpy as np

image = cv2.imread('ok.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# base = [[213, 227, 380, 3688]]


# Find contours and extract the bounding rectangle coordintes
# then find moments to obtain the centroid
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
bbox = []
keep = []

# print(cnts)
# print("-" * 70)
# print(cnts2)

for c in cnts:
    # Obtain bounding box coordinates and draw rectangleq
    x, y, w, h = cv2.boundingRect(c)
    bbox.append(x)
    bbox.append(y)
    bbox.append(w)
    bbox.append(h)
    cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
    # print("x: {} y: {} w: {} h: {}".format(x, y, w, h))
    # print(base)
    # print("^" * 80)
    print(bbox)
    # print(type(bbox))
    # print("^" * 80)
    # print(bbox[0])
    # print(type(bbox))
    #
    # print(base[0])
    # print(type(bas))
    #
    # print("^" * 80)

    # เทียบความเท่ากันทั้งคู่
    # if set(bas).issubset(bbox):
    #     print('OKKK')
    # else:
    #     print("NOOOOO")

    # 240 - 20 = 220
    # 240 + 20 = 260
    base = [212, 220, 383, 372]

    # base2 = [240, 1300, 121, 215]
    count = 0
    db = []
    # เก็บเป็นช่วง
    # if base[0] - 20 <= bbox[0] <= base[0] + 20:
    #     print("OKKK")
    # else:
    #     print("NOOOO")

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
    else:
        print("ERROR")

    if count == 4:
        db.append(1)
        print("Count is : {} ".format(count))
        print("Success")
    else:
        print("Count is : {} ".format(count))
        print("Error")

    # count = 0
    # for i in base:
    #     for n in base2:
    #         print("i: {} n: {}".format(i, n))
    #         if i >= n:
    #             print("OOOKKK")
    #             print("-" * 100)
    #             count += 1
    #         else:
    #             print("Noooooo")
    #             print("*" * 100)
    #             count += 1
    # print(count)

#
# Find center coordinate and draw center point
# M = cv2.moments(c)
# cx = int(M['m10'] / M['m00'])
# cy = int(M['m01'] / M['m00'])
# tt = cv2.circle(image, (cx, cy), 2, (36, 255, 12), -1)
# tt2 = cv2.circle(image, (150, 300), 2, (36, 255, 12), -1)
# center = cx, cy
# # print('Center: ({}, {})'.format(center[0], center[1]))
# print(type(center))
# print(cx)

# cv2.imshow('image', image)
# cv2.imshow('img2', gray)
# cv2.imshow('img3', image)
#
# cv2.waitKey()
# print(image)
