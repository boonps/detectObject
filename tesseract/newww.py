import cv2
from PIL import Image
import pytesseract
# Importing the Opencv Library
import numpy as np

# Importing NumPy,which is the fundamental package for scientific computing with Python
# Reading Image
img = cv2.imread("test2.jpeg")
img2 = cv2.imread("test2.jpeg")
# cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
cv2.imshow("Original Image", img)
# Display image
# RGB to Gray scale conversion
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.namedWindow("Gray Converted Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Gray Converted Image",img_gray)
# Display Image
# Noise removal with iterative bilateral filter(removes noise while preserving edges)
noise_removal = cv2.bilateralFilter(img_gray, 9, 75, 75)
# cv2.namedWindow("Noise Removed Image",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Noise Removed Image",noise_removal)
# Display Image
# Histogram equalisation for better results
equal_histogram = cv2.equalizeHist(noise_removal)
# cv2.namedWindow("After Histogram equalisation",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("After Histogram equalisation",equal_histogram)
# Display Image
# Morphological opening with a rectangular structure element
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
morph_image = cv2.morphologyEx(equal_histogram, cv2.MORPH_OPEN, kernel, iterations=15)
# cv2.namedWindow("Morphological opening",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Morphological opening",morph_image)
# Display Image
# Image subtraction(Subtracting the Morphed image from the histogram equalised Image)
sub_morp_image = cv2.subtract(equal_histogram, morph_image)
# cv2.namedWindow("Subtraction image", cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Subtraction image", sub_morp_image)
# Display Image
666  # Thresholding the image
ret, thresh_image = cv2.threshold(sub_morp_image, 0, 255, cv2.THRESH_OTSU)
# cv2.namedWindow("Image after Thresholding",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Image after Thresholding",thresh_image)
# Display Image
# Applying Canny Edge detection
canny_image = cv2.Canny(thresh_image, 250, 255)
# cv2.namedWindow("Image after applying Canny",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Image after applying Canny",canny_image)
# Display Image
canny_image = cv2.convertScaleAbs(canny_image)
# dilation to strengthen the edges
kernel = np.ones((3, 3), np.uint8)
# Creating the kernel for dilation
dilated_image = cv2.dilate(canny_image, kernel, iterations=1)
# cv2.namedWindow("Dilation", cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Dilation", dilated_image)
# Displaying Image
# Finding Contours in the image based on edges
contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
print(len(contours))
# Sort the contours based on area ,so that the number plate will be in top 10 contours
screenCnt = None
# loop over our contours
for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.06 * peri, True)  # Approximating with 6% error
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:  # Select the contour with 4 corners
        screenCnt = approx
        break
final1 = cv2.drawContours(img, screenCnt, -1, (0, 255, 0), 3)
# x, y, width, height = cv2.boundingRect([screenCnt])
# print (x,y)
# Drawing the selected contour on the original image
# cv2.namedWindow("Image with Selected Contour",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Image with Selected Contour",final)
# Masking the part other than the number plate
mask = np.zeros(img_gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(img, img, mask=mask)
# cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
cv2.imshow("Final_image", new_image)
print(screenCnt[0])
pts1 = np.float32((screenCnt[0], screenCnt[3], screenCnt[1], screenCnt[2]))
pts2 = np.float32([[0, 0], [400, 0], [0, 150], [400, 150]])
print(pts1)
print(pts2)
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(new_image, M, (400, 150))
# cv2.namedWindow("Finally_image",cv2.WINDOW_NORMAL)
cv2.imshow("Finally_image", dst)
cv2.imwrite('out.jpg', dst)
im_gray = cv2.imread('out.jpg', 0)
# th3 = cv2.adaptiveThreshold(im_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
ret, th3 = cv2.threshold(im_gray, 100, 255, cv2.THRESH_BINARY)
cv2.imwrite('out_gray.jpg', th3)
crop_img = th3[17:160, 20:375]  # Crop from x, y, w, h -> 100, 200, 300, 400
# roi = im[y1:y2, x1:x2]
cv2.imshow("Finally_image_", crop_img)
cv2.imwrite('out_gray.jpg', crop_img)
final = cv2.drawContours(img2, [screenCnt], -1, (0, 255, 0), 3)
x = pytesseract.image_to_string(Image.open('out_gray.jpg'), lang='tha')
print(x)
cv2.putText(final, 'Taipe' + "s" + " Arduino and Raspberry Pi", (50, 375), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 127))
cv2.imshow("Image with Selected Contour", final)
# Histogram equal for enhancing the number plate for further processing
# y,cr,cb = cv2.split(cv2.cvtColor(new_image,cv2.COLOR_RGB2YCrCb))
# Converting the image to YCrCb model and splitting the 3 channels
# y = cv2.equalizeHist(y)
# Applying histogram equalisation
# final_image = cv2.cvtColor(cv2.merge([y,cr,cb]),cv2.COLOR_YCrCb2RGB)
# Merging the 3 channels
# cv2.namedWindow("Enhanced Number Plate",cv2.WINDOW_NORMAL)
# Creating a Named window to display image
# cv2.imshow("Enhanced Number Plate",final_image)
# Display image
cv2.waitKey()  # Wait for a keystroke from the user
