import cv2
import numpy as np
import cv2 as cv

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread('ttt.jpeg')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = detect.detectMultiScale(img, 1.3, 5)

start = (384, 0)
end = (510, 128)

start1 = (0, 100)
end1 = (100, 0)

name = []
name2 = []
pp = 0
dd = 0


# print("{} -- {},{}".format(name, start, end))


def markAttendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
        nameList.append(entry[0])
        if name not in nameList:
            coords1 = start
            coords2 = end
        f.writelines(f'\n{name},{coords1},{coords2}')
    # print(myDataList)


if pp == 0:
    d = cv.rectangle(img, start, end, (0, 0, 255), 3)
else:
    do = cv.rectangle(img, start, end, (0, 255, 0), 3)
    name.append(1)
    markAttendance(name)

cv.imshow("immmmm", img)

k = cv.waitKey(0)
if k == ord("q"):
    cv.destroyAllWindows()
