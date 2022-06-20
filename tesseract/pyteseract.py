import cv2
import imutils
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"
img = cv2.imread('../OpenCV_3_License_Plate_Recognition_Python-master/LicPlateImages/car4.jpeg')
carplate_haar_cascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# th = cv2.threshold(gray, 0, 200, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.bilateralFilter(gray, 13, 15, 15)
edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        print(screenCnt)
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

text = pytesseract.image_to_string(Cropped, config='--psm 11')
print("programming_fever's License Plate Recognition\n")
print("Detected license plate Number is:", text)

hImg, wImg, _ = img.shape
conf = r'-l tha --psm 6'

boxes = pytesseract.image_to_boxes(gray, config=conf)
names = []
for b in boxes.splitlines():
    # print(b)
    names.append(b[0])
    b = b.split(' ')
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
    cv2.putText(img, str(names), (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

print('{}'.format(names))

# cv2.imshow("img", img)
cv2.imshow("img2", gray)

cv2.imshow("img4", edged)
cv2.waitKey(0)
