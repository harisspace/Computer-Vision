# rescale dimention
import cv2 as cv

def rescale_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimentions = (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

# rescale the images
# img = cv.imread('Resources/Photos/cat.jpg')

# img_rescale = rescale_frame(img)
# cv.imshow('Cat', img)
# cv.imshow('Cat_rescale', img_rescale)

# cv.waitKey(0)

# using capture.set
def changeRes(width, height):
    # for live video
    capture.set(3, width)
    capture.set(4, height)

# rescale the videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resize = rescale_frame(frame, 0.2)

    cv.imshow('dog_rescale', frame_resize)
    cv.imshow('dog', frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.realese()
cv.destroyAllWindows()


    