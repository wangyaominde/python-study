# @Author: wangyaominde
# @Date: 2019-01-03 16:47:57
# @Last Modified by:   wangyaominde
# @Last Modified time: 2019-01-03 16:47:57
import serial.tools.list_ports
import serial
import string
import binascii

class Ser(object):
    def __init__(self,name):
        self.name=name
class name(Ser):
    def __init__(self,name,bundrate):
        self.name = name
        self.bundrate = 9600


Switchname = "CH340"
Switchbundrate = 9600
def getsername():
    Com_Dict = {}
    port_list = list(serial.tools.list_ports.comports())
    for port in port_list:
                Com_Dict["%s" % port[1]] = "%s" % port[1]
                if(Switchname in port[1]):
                    return(port[0])


switchser = serial.Serial(getsername(),Switchbundrate)
switchser.open
