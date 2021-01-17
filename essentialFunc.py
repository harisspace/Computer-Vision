# grayscale
import cv2 as cv

img = cv.imread("Resources/Photos/park.jpg")
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 125)
cv.imshow('Canny', canny)  

# dilating
dilated = cv.dilate(canny, (7, 7), iterations=2)
cv.imshow('Dilated', dilated)

# eroded
eroded = cv.erode(dilated, (7, 7), iterations=2)
cv.imshow('eroded', eroded)

# resized
resize = cv.resize(img, (300, 300), interpolation=cv.INTER_AREA)
cv.imshow('resize', resize)

# crop
crop = img[0:200, 0:400]
cv.imshow('crop', crop)


cv.waitKey(0)

