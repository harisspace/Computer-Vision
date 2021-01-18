import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
print(lap)
print(np.absolute(lap))
lap = np.uint8(np.absolute(lap))

cv.imshow('laplacian', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)

# merge sobel
merge = cv.bitwise_or(sobelx, sobely)
cv.imshow('merge', merge)

cv.waitKey(0)