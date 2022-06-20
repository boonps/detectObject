import cv2


def calculateIntersection(a0, a1, b0, b1):
    if a0 >= b0 and a1 <= b1:  # Contained
        intersection = a1 - a0
    elif a0 < b0 and a1 > b1:  # Contains
        intersection = b1 - b0
    elif a0 < b0 and a1 > b0:  # Intersects right
        intersection = a1 - b0
    elif a1 > b1 and a0 < b1:  # Intersects left
        intersection = b1 - a0
    else:  # No intersection (either side)
        intersection = 0

    return intersection


axfix, ayfix, awfix, ahfix = [187, 279, 335, 394]
# roi = frame[y:y + h, x:x + w]
ax, ay, aw, ah = [240, 340, 286, 360]
bx, by, bw, bh = [313, 336, 351, 352]
cx, cy, cw, ch = [381, 336, 427, 352]
dx, dy, dw, dh = [445, 331, 484, 343]

AREAa = float((aw - ax) * (ah - ay))
AREAafix = float((awfix - axfix) * (ahfix - ayfix))
AREAb = float((bw - bx) * (bh - by))
AREAc = float((cw - cx) * (ch - cy))
AREAd = float((dw - dx) * (dh - dy))

intersecting = []

cap = cv2.VideoCapture("pk_2.mp4")
car_cas = cv2.CascadeClassifier('car.xml')

while True:
    ret, frame = cap.read()

    axfix, ayfix, awfix, ahfix = [187, 279, 335, 394]
    roi = frame[ayfix:ayfix + ahfix, axfix:axfix + awfix]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray, (21, 21), 0)

    cars = car_cas.detectMultiScale(roi, 1.1, 1)

    # aa = cv2.rectangle(frame, (240, 340), (286, 360), (0, 0, 255), 3)
    bb = cv2.rectangle(frame, (313, 336), (351, 352), (0, 0, 255), 3)
    cc = cv2.rectangle(frame, (381, 336), (427, 352), (0, 0, 255), 3)
    dd = cv2.rectangle(frame, (445, 331), (484, 343), (0, 0, 255), 3)
    ddd = cv2.rectangle(frame, (242, 134), (266, 158), (255, 255, 255), 3)

    # contours, _ = cv2.findContours(cars, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # for cnt in contours:
    #
    #     area = cv2.contourArea(cnt)
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    for (x, y, w, h) in cars:
        pp = cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("({}), ({})".format(pp[1], pp[2]))
        if len(cars) > 0:
            width = calculateIntersection(x, w, ax, aw)
            height = calculateIntersection(y, h, ay, ah)
            area = width * height
            percent = (area / AREAa) * 100
            if area >= AREAafix:
                print("OOOOKKKK")
                if (percent >= 80):
                    aa = cv2.rectangle(frame, (240, 340), (286, 360), (255, 255, 255), 3)
                    intersecting.append([x, y, w, h])
                    intersecting.append([1])
                    print("\n" * 3)

        cv2.imshow("FRAME", frame)
        cv2.imshow("FRAME7", roi)
        # print(intersecting)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
