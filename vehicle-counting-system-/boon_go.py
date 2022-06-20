import cv2
import numpy as np

# ใช้กำหนดขนาดวัตถุที่จะดีเทค
min_contour_width = 40  # 40
min_contour_height = 40  # 40

# ขนาดความสูงต่ำของเส้น
line_height = 440  # 550

matches = []

offset = 10  # 10
cars = 0


# ฟังก์ชั่นการหากึ่งกลาง
def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)

    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('traffic.mp4')

# cap.set(3, 1920)
# cap.set(4, 1080)
#
# if cap.isOpened():
#     ret, frame1 = cap.read()
# else:
#     ret = False

# ในส่วนนี้ถ้าเปิดขึ้นให้นำภาพมาต่อกันเป็นเฟรมไปเรื่อยๆพร้อมๆกัน เพื่อเปรียบเทียบ
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while ret:
    d = cv2.absdiff(frame1, frame2)
    grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(th, np.ones((3, 3)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

    # อตรวจจับรถและวาดสี่เหลี่ยมให้เท่ากับขนาดโดยห่างออกไป10โดยกำหนดจากกึ่งกลาง
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
    contours, h = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print(contours, h)
    # ตรวจสอบค่า index และเก็บค่าพิกัดเข้าไป
    for (i, c) in enumerate(contours):  # index , value
        (x, y, w, h) = cv2.boundingRect(c)
        contour_valid = (w >= min_contour_width) and (
                h >= min_contour_height)
        # หาก w h ไม่เป็นไปตามเงื่อนไขให้ทำต่อไปเรื่อยๆ
        if not contour_valid:
            continue
        #     สร้างสี่เหลี่ยมครอบวัตถุที่ผ่านไปโดยเว้นระยะออกไปอย่างละ10
        cv2.rectangle(frame1, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)

        # วาดเส้นขึ้นเพื่อรอตรวจจับรถ
        cv2.line(frame1, (0, line_height), (1200, line_height), (0, 255, 0), 2)
        # นำค่าใส่ไปที่ฟังก์ชั่นทำกึ่งกลาง
        centroid = get_centroid(x, y, w, h)
        # เพิ่มค่จุดกึ่งกลางที่ได้จากการคำนวณฟังก์ชั่นเข้าตัวแปล  แต่จะเพิ่มเข้าเรื่อยๆ
        matches.append(centroid)
        # print(matches)

        # เพิ่มจุดกึ่งกลางเข้าไปในวีดีโอ
        cv2.circle(frame1, centroid, 5, (0, 255, 0), -1)

        # รับค่าจากฟังก์ชั่นมา
        cx, cy = get_centroid(x, y, w, h)
        ###### ฟังก์ชั่นนับรถ ######
        for (x, y) in matches:
            # จะนับว่าจริงก็ต่อเมื่อแกรไวของเกึ่งกลางอยู่ในช่วงระกว่าไม่เกินเส้นเขียว +- 10
            # if y < (line_height + offset) and y > (line_height - offset):
            if y == (line_height + offset):
                cars = cars + 1
                #############################
                # ที่ต้องมีฟังก์ชั่นนี้เพราะว่าจะเริ่มนับเมื่อจุดกึ่งกลางเหมือนกับจุดกลึ่งกลางที่ตั้งไว้ในเส้นเท่านั้นถึงจะนับเป็น1
                # ถ้าไม่นั้นมันจะนับตั้งแต่เกิดจุดกึ่งกลางตั้งแต่ดีเทครถได้ไกลๆ
                #############################
                matches.remove((x, y))
                print(cars)

    cv2.putText(frame1, "Total Cars Detected: " + str(cars), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 170, 0), 2)

    cv2.putText(frame1, "TY Bro", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 170, 0), 2)

    cv2.imshow("Image", frame1)
    cv2.imshow("Differance", th)

    if (cv2.waitKey(1) & 0xFF == ord("q")):
        break
        # ช่วงนี้มาเพื่อนำเฟรมที่กำหนดไว้มาต่อกันเป็นวีดีโอ
    frame1 = frame2
    ret, frame2 = cap.read()
cap.release()
cv2.destroyAllWindows()
