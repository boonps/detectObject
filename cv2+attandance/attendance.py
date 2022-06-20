import os
import face_recognition as facer
import numpy as np
import cv2

oat_image = facer.load_image_file("ImagesAttendance/ate.jpeg")
oat_image = cv2.cvtColor(oat_image, cv2.COLOR_BGR2RGB)

oat_test = facer.load_image_file("ImagesAttendance/oat2.jpeg")
oat_test = cv2.cvtColor(oat_test, cv2.COLOR_BGR2RGB)

ids = '1'
ids2 = '2'
faceloc = facer.face_locations(oat_image)[0]
encodoat = facer.face_encodings(oat_image)[0]
cv2.rectangle(oat_image, "ids2", (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), [255, 0, 255], 2)

faceloctest = facer.face_locations(oat_test)[0]
encodoattest = facer.face_encodings(oat_test)[0]

cv2.rectangle(oat_test, "ids", (faceloctest[3], faceloctest[0]), (faceloctest[1], faceloctest[2]), [255, 0, 255], 2)
print(faceloc)


result = facer.compare_faces([encodoat], encodoattest)
face_dis = facer.face_distance([encodoat], encodoattest)
print(result, face_dis * 100)

cv2.imshow("result", oat_image)
cv2.imshow("result2", oat_test)
cv2.waitKey(0)
