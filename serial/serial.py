# @Author: wangyaominde
# @Date: 2019-01-03 11:11:36
# @Last Modified by:   wangyaominde
# @Last Modified time: 2019-01-03 11:11:36
# 发送和接收16进制的
#%%
import serial
import string
import binascii
ser = serial.Serial('COM8', 9600)
ser.open()
#%%
'''
#接收
n = ser.inwaiting()
if n:
    data = str(binascii.b2a_hex(ser.read(n)))[2:-1]
    print(data)
#发送
'''
#%%
ser.write(bytes.fromhex('a0 01 01 a2'))     #接通A
#%%
ser.write(bytes.fromhex('a0 02 01 a3'))     #接通B
#%%
ser.write(bytes.fromhex('a0 01 00 a1'))     #断开A
#%%
ser.write(bytes.fromhex('a0 02 00 a2'))     #断开B
#ser.close()
