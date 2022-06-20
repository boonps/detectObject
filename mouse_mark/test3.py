import cv2

img = cv2.imread("ttt.jpeg")
detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

start = (540, 12)
end = (591, 63)
dev = []

face = detect.detectMultiScale(img)


# if 1 in face:
#     dev.append(3)


# print(dev)
# print(face)
print(detect)
# if face <= [0]:
#     dev.append(3)


# def oat():
#     cm = cv2.rectangle(img, start, end, (0, 255, 0), 3)
#     return cm


# oat()


# if dev == [3]:
#     cv2.rectangle(img, start, end, (0, 0, 255), 3)
#     print("4444")

# for x, y, w, h in face:
#     aa = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
# print(x, y, w, h)

cv2.imshow('out_put', img)
cv2.waitKey()
cv2.destroyAllWindows()
