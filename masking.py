import numpy as np
import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

circle = cv.circle(blank.copy(), (200, 200), 170, 255, -1)
cv.imshow('circle', circle)

masking = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masking', masking)

rectangle = cv.rectangle(blank.copy(), (30,30), (200, 200), 255, thickness=-1)
cv.imshow('rectangle', rectangle)

weird_shape = cv.bitwise_and(rectangle, circle)
cv.imshow('weird', weird_shape)

if cv.waitKey(20) == ord('s'):
    cv.destroyAllWindows()

cv.waitKey(0)