import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg', 0)

cv.imshow('Boston', img)

# transformation
# translation
rows, cols = img.shape
x = 50
y = 100
M = np.float32([[1,0,x], [0,1,y]])
dst = cv.warpAffine(img, M, (cols, rows))
print(dst)
cv.imshow('translated', dst)

# rotated
M = cv.getRotationMatrix2D((cols //2, rows // 2), 45, 1)
rotated = cv.warpAffine(img, M, (cols, rows))
cv.imshow('rotated', rotated)

# resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# flipping
# 1 horizontal and -1 vertikal
flip = cv.flip(img, -1)
cv.imshow('flip', flip)

#cropping
crop = img[100:200, 200:300]
cv.imshow('croped', crop)

cv.waitKey(0)



