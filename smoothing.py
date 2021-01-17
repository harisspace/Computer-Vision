import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')

# blur => that is average
average = cv.blur(img, (5,5))
cv.imshow('blur', average)

# gaussianBlur
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('gauss', gauss)

# median
median = cv.medianBlur(img, 5)
cv.imshow('median', median)

# bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 50)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)