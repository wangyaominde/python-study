# @Author: wangyaominde  
# @Date: 2019-01-03 11:11:36  
# @Last Modified by:   wangyaominde  
# @Last Modified time: 2019-01-03 11:11:36
# 发送和接收16进制的
import serial
import string
import binascii
s = serial.Serial('com4', 9600)
s.open()
#接收
n = s.inwaiting()
if n:
    data = str(binascii.b2a_hex(s.read(n)))[2:-1]
    print(data)
#发送
s.write(bytes.fromhex('10 11 12 34 3f'))
s.close()
