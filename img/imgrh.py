#coding=utf-8
#基于PIL的像素点的图像融合 基于pyhton2
from PIL import Image
import math
import sys
pic1 = raw_input("Please input pic1:")	#输入图1的名字
pic2 = raw_input("Please input pic2:")	#输入图2的名字
qz1 = input("Please input pic1`s proportion:")		#输入图1的比例
qz2 = input("Please input pic2`s proportion:")		#输入图2的比例
ou = raw_input("Please input your after process file name:")	#输入保存的文件的名称
t = Image.open(pic1)		#打开图1
y = Image.open(pic2)		#打开图2
l = t.convert('RGB')			#强制转换为rgb
g = y.convert('RGB')
size = l.size		#将图1的size设为输出的size
o = Image.new('RGB',size)	#建立需要输出的图像
width = l.size[0]
height = l.size[1]
if (width>height):
	width,height=height,width
print "/*	width: %d	*/"%(size[0]) 	#输出目标的宽
print "/*	height: %d	*/"%(size[1])   #输出目标的高
for h in range(0,height):
	for w in range(0,width):				#遍历所有像素
		rl = l.getpixel((w,h))[0]			#输出图1的r通道的像素点
		gl = l.getpixel((w,h))[1]			#输出图1的g通道的像素点
		bl = l.getpixel((w,h))[2]			#输出图1的b通道的像素点
		#print '%d,%d,%d'%(rl,gl,bl)		#可以看见分离后的像素点
		rg = g.getpixel((w,h))[0]
		gg = g.getpixel((w,h))[1]
		bg = g.getpixel((w,h))[2]
		ro = int(rl*qz1+rg*qz2)				#将图一和图二按照4:6进行融合，并且转换为整型数
		go = int(gl*qz1+gg*qz2)
		bo = int(bl*qz1+bg*qz2)
		o.putpixel((w,h),(ro,go,bo))		#将所有得到的像素点按照w，h进行填充
o.save(ou)							#保存为名为用户输入的文件
