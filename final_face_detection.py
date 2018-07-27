import numpy as np
import cv2

cap = cv2.VideoCapture('C:\Users\TEJAS\Downloads\vid1')
face_cascade = cv2.CascadeClassifier('C:\\Users\\TEJAS\\Downloads\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\TEJAS\\Downloads\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('face.mp4',fourcc, 25.0, (640,480))
cap.open('C:\Users\TEJAS\Downloads\vid1')
while 1:
    ret, img = cap.read()
    print 'hello'
    if ret==True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
            #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        out.write(img)

        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
