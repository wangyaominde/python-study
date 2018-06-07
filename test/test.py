import cv2
import numpy

cap = cv2.VideoCapture(0)

while 1:
     ret, frame = cap.read()
     cv2.imshow("test",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
