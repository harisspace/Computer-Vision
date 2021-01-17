# # latihan day one

# # open image
# # import cv2 as cv

# # img = cv.imread('Resources/Photos/cat.jpg')

# # cv.imshow('Cat', img)

# # cv.waitKey(0)

# # open video

# # import cv2 as cv

# # capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# # while True:
# #     isTrue, img = capture.read()

# #     cv.imshow('Dog', img)

# #     if cv.waitKey(20) & 0xff == ord('d'):
# #         break

# # capture.realease()
# # cv.destroyAllWindows()


# # resize
# # import cv2 as cv

# # def resize_capt(frame, scale = 0.5):
# #     width = int(frame.shape[1] * scale)
# #     height = int(frame.shape[0] * scale)

# #     dimentions = (width, height)

# #     return cv.resize(frame, dimentions, interpolation = cv.INTER_AREA)

# # img = cv.imread('Resources/Photos/cat.jpg')
# # resize_img = resize_capt(img)
# # cv.imshow('Cat', img)
# # cv.imshow('Cat resize', resize_img)

# # cv.waitKey(0)


# # latihan day 2

# # how to draw
# import cv2 as cv
# import numpy as np

# blank = np.zeros((400, 400, 3), 'uint8')

# # coloring
# blank[:] = 0, 0, 255
# cv.imshow('blank', blank)

# # rectangular
# rectangle = cv.rectangle(blank, (0, 0), (200, 200), (0, 255, 255), thickness=cv.FILLED)
# cv.imshow('rectangle', rectangle)

# # circle
# circle = cv.circle(blank, (200, 200), 40, (255, 255, 255), thickness=cv.FILLED)
# cv.imshow('circle', circle)

# # line 
# line = cv.line(blank, (200, 200), (100, 100), (0, 0, 0), thickness=3)
# cv.imshow('line', line)

# # put text
# text = cv.putText(blank, "haii this is haris", (0, 200), cv.FONT_HERSHEY_TRIPLEX, 1.2, (0, 0, 0))
# cv.imshow('text', text)

# cv.waitKey(0)

# essentioal func
import cv2 as cv

img = cv.imread("Resources/Photos/park.jpg")

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 125)
cv.imshow('canny', canny)

# dilating
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow('dilated', dilated)

# eroded
eroded = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow('eroded', eroded)

# resized
resize = cv.resize(img, (300, 200), interpolation=cv.INTER_AREA)
cv.imshow('resize', resize)

# crop
crop = img[0:200, 100:300]
cv.imshow('crop', crop)

cv.waitKey(0)


