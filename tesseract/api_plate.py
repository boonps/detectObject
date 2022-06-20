# # Import dependencies
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2  # This is the OpenCV Python library
# import pytesseract  # This is the TesseractOCR Python library
#
# pytesseract.pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"
#
# carplate_img = cv2.imread('car4.jpeg')
# carplate_img_rgb = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
# # plt.imshow(carplate_img_rgb)
#
# carplate_haar_cascade = cv2.CascadeClassifier('haarcascade_licence_plate_rus_16stages.xml')
#
#
# # Setup function to detect car plate
# def carplate_detect(image):
#     carplate_overlay = image.copy()
#     carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay, scaleFactor=1.1, minNeighbors=3)
#
#     for x, y, w, h in carplate_rects:
#         cv2.rectangle(carplate_overlay, (x, y), (x + w, y + h), (255, 0, 0), 5)
#
#         return carplate_overlay
#
#
# detected_carplate_img = carplate_detect(carplate_img_rgb)
# plt.imshow(detected_carplate_img)
# plt.show()
import cv2
import numpy as np
import json
import matplotlib.pyplot as plot
import matplotlib.patches as patches
import requests


images = cv2.imread('../OpenCV_3_License_Plate_Recognition_Python-master/LicPlateImages/car4.jpeg')
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
th = cv2.threshold(gray, 0, 200, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]


url = "https://api.aiforthai.in.th/lpr-v2"

files = {'image': open('../OpenCV_3_License_Plate_Recognition_Python-master/LicPlateImages/car4.jpeg', 'rb')}

headers = {
    'Apikey': "bZ3T8LvmXUoTIoej9ufyhMLHrSByWBGX",
}

response = requests.post(url, files=files, headers=headers)

print(response.json())

data = response.json()
for item in data:
    _object = (item['lpr'])
    xLeftTop = int(item['bbox']['xLeftTop'])
    yleftTop = int(item['bbox']['yLeftTop'])
    xRightBottom = int(item['bbox']['xRightBottom']) / 3
    yRightBottom = int(item['bbox']['yRightBottom']) / 3

    figure, get_axis = plot.subplots(1)
    get_axis.imshow(images)
    rect = patches.Rectangle((xLeftTop, yleftTop), xRightBottom, yRightBottom, linewidth=5, edgecolor='#7FFF00',
                             facecolor='none')
    get_axis.add_patch(rect)
    plot.text(xLeftTop, yleftTop - 50, _object, fontname='Tahoma', fontsize='20', color='#7FFF00')
    plot.show()
