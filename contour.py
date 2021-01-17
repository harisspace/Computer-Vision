import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# # canny
# canny = cv.Canny(blur, 100, 100, cv.BORDER_DEFAULT)
# cv.imshow('canny', canny)

# selain canny ada juga namanya tresholding
ret, tresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# count the contour
contours, hierarchies = cv.findContours(tresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'{hierarchies} the contour is')

# draw the countour
draw = cv.drawContours(blank, contours, -1, (0,0,255), thickness=1)
cv.imshow('draw', draw)

cv.imshow('tresh', tresh)



cv.waitKey(0)

