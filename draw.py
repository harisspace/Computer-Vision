import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# img = cv.imread('Resources/Photos/cat.jpg')

# coloring
# blank[:] = 0, 0, 255
# cv.imshow('Green', img)

# draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow("rectangle", blank)

# draw circle

cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 100, (255, 255, 255), thickness=-1)
cv.imshow('circle', blank)

# draw the line

cv.line(blank, (10, 0), (100, 20), (0, 0, 0), thickness=3)
cv.imshow('line', blank)

# put text

cv.putText(blank, "HAII GUYSS THIS IS OPENCV", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.2, (0, 255, 0))
cv.imshow('text', blank)

cv.waitKey(0)