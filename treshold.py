import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# simple tresh
threshold, thresh = cv.threshold(gray, 170, 255, cv.THRESH_BINARY)
print(threshold)
cv.imshow('thres', thresh)
# invers
threshold_inv, thres_inv = cv.threshold(gray, 170, 255, cv.THRESH_BINARY_INV)
cv.imshow('thres_inv', thres_inv)

# adaptive thresh
adapt = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adapt', adapt)

# adaptive gaus
adapt_gaus = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('gauss', adapt_gaus)





cv.waitKey(0)