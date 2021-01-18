import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# histogram
img = cv.imread('Resources/Photos/cats.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# coba = np.array([0,20])

# gray_hist = cv.calcHist([img], [0], None, [256], [0,256])
# print(gray_hist)

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# # plt.xlim([0,100])
# plt.show()

# color histogram
plt.figure()
plt.title('Colors Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    print(col)
    plt.plot(hist, color=col)
    plt.xlim([0,256])
    
plt.show()
