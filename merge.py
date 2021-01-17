import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

# learn how to split channel and merge
b, g, r = cv.split(img) # bgr because default of opencv is bgr

cv.imshow('img', img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

# merge
merge = cv.merge([b,g,r])
cv.imshow('merge', merge)

# and you can see the color using blank
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)



if cv.waitKey(20) == ord('s'):
    cv.destroyAllWindows()

cv.waitKey(0)
