#coding=utf-8
#基于opencv的像素点的图像融合 基于pyhton3
import cv2    
import numpy
pic1 = input("Please input pic1:")	#输入图1的名字
pic2 = input("Please input pic2:")	#输入图2的名字
qz1 = eval(input('Please input pic1`s proportion:'))
qz2 = eval(input('Please input pic2`s`s proportion:'))

'''qz1 = input("Please input pic1`s proportion:")		#输入图1的比例
qz2 = input("Please input pic2`s proportion:")		#输入图2的比例'''
p1 = cv2.imread(pic1)
p2 = cv2.imread(pic2)
#high = cv2.imread("high.jpg",cv2.IMREAD_COLOR)
#low = cv2.imread("low.jpg",cv2.IMREAD_COLOR)  
#im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   #转换了灰度化
print ("p1:\n")  
print (p1.shape)
print (p1.size)
print (p1.dtype)
print ("p2:\n")
print (p2.shape)
print (p2.size)
print (p2.dtype)
img_mix = cv2.addWeighted(p1, qz1, p2, qz2, 0)
cv2.imshow('img_mix', img_mix)
cv2.imshow("HIGH",p1)
cv2.imshow("low",p2)    
cv2.waitKey(0) 
cv2.destroyAllWindows()  