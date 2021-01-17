import numpy as np
import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# circle = cv.circle()

if cv.waitKey(20) == ord('s'):
    cv.destroyAllWindows()

cv.waitKey(0)