# @Author: wangyaominde
# @Date: 2019-01-03 16:47:57
# @Last Modified by:   wangyaominde
# @Last Modified time: 2019-01-03 16:47:57
import serial.tools.list_ports
import serial
import string
import binascii
import time

class Ser(object):
    def __init__(self,name,bundrate):
        self.name = name
        self.bundrate = bundrate


class switch(Ser):
    name = "CH340"
    bundrate=9600




def getsername():
    Com_Dict = {}
    port_list = list(serial.tools.list_ports.comports())
    for port in port_list:
                Com_Dict["%s" % port[1]] = "%s" % port[1]
                if(switch.name in port[1]):
                    return(port[0])


switchser = serial.Serial(getsername(),switch.bundrate)
for i in range(10):
    switchser.write(bytes.fromhex('a0 01 01 a2'))     #接通A
    switchser.write(bytes.fromhex('a0 02 01 a3'))     #接通B
    switchser.write(bytes.fromhex('a0 01 00 a1'))     #断开A
    switchser.write(bytes.fromhex('a0 02 00 a2'))     #断开B




switchser.open
