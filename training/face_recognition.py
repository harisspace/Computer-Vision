import numpy as np
import cv2 as cv

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_recog.yml')

img = cv.imread(r'C:\coding\python\openCVtuts\Resources\Faces\val\ben_afflek\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face_rect:
    face_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(face_roi)
    print(f'label = {label} with confidence = {confidence}')

    cv.rectangle(img, (x,y), (x+w, y+h), (0,255, 0), thickness=3)
    cv.putText(img, str(people[label]), (x-10,y-10), cv.FONT_HERSHEY_COMPLEX, 1.1, (0,255,0), 3)

cv.imshow('img', img)
cv.waitKey(0)