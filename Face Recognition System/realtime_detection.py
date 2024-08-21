import numpy as np
import cv2
import os

faceCascade = cv2.CascadeClassifier(r'C:\Users\hp\Downloads\Vinayan_New\Face Recognition System\OpenCV-Face-Recognition\FaceDetection\Cascades\haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('rtsp://admin:vinayan@123@192.168.1.64:554/1/1')
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    if not ret:
        pass
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]  
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()