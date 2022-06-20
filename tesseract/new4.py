# import cv2
# import imutils
# import numpy as np
# import pytesseract
#
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
#
# img = cv2.imread('car.jpeg', cv2.IMREAD_COLOR)
# img = cv2.resize(img, (620, 480))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale
# gray = cv2.bilateralFilter(gray, 13, 15, 15)
# edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
#
# contours = cv2.findContours(edged.copy(), cv2.RETR_TREE,
#                             cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(contours)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
# screenCnt = None
#
# for c in contours:
#     # approximate the contour
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.018 * peri, True)
#     # if our approximated contour has four points, then
#     # we can assume that we have found our screen
#     # print(approx)
#     if len(approx) == 4:
#         screenCnt = approx
#         break
#
# # Masking the part other than the number plate
# mask = np.zeros(gray.shape, np.uint8)
# new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
# new_image = cv2.bitwise_and(img, img, mask=mask)
#
# (x, y) = np.where(mask == 255)
# (topx, topy) = (np.min(x), np.min(y))
# (bottomx, bottomy) = (np.max(x), np.max(y))
# Cropped = gray[topx:bottomx+1, topy:bottomy+1]
#
# print(Cropped)
#
#
# cv2.imshow('car', img)
# cv2.imshow('car1', Cropped)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')

img = cv2.imread('../OpenCV_3_License_Plate_Recognition_Python-master/LicPlateImages/car4.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2,
                                     minNeighbors=5, minSize=(25, 25))

for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
    plate = gray[y: y + h, x:x + w]
    plate = cv2.blur(plate, ksize=(20, 20))
    # put the blurred plate into the original image
    gray[y: y + h, x:x + w] = plate

cv2.imshow('plates', gray)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
