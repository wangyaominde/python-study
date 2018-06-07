# -*- coding: utf-8 -*-  
import cv2  
import numpy as np    
import socket
import struct

cap = cv2.VideoCapture(0)
#s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while (1):
    _, image = cap.read()
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=30,minRadius=90,maxRadius=100)   
    if circles is not None:
         circles = np.round(circles[0, :]).astype("int")
         for (x, y, r) in circles:
             cv2.circle(output, (x, y), r, (0, 255, 0), 4)
             cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
             print(x,y)#输出圆心坐标
             #s.sendto(struct.pack('ii',x,y),("192.168.31.70",5000))
    cv2.imshow("output", np.hstack([image, output]))
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()  

