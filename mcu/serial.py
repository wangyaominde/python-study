#-*-coding:utf-8-*-   
#基于python的串口检测程序
import serial  

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)   
data=''
while (1):
    data+=ser.read(10)
    if data!='':
        print data
    else :
          print 'nothing'
