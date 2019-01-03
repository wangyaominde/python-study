# @Author: wangyaominde
# @Date: 2019-01-03 16:47:57
# @Last Modified by:   wangyaominde
# @Last Modified time: 2019-01-03 16:47:57

import serial.tools.list_ports

restemser = "CH340"
Com_Dict = {}
port_list = list(serial.tools.list_ports.comports())
for port in port_list:
            Com_Dict["%s" % port[1]] = "%s" % port[1]
            if(restemser in port[1]):
                print(port[0])

port
port[1]
port[0]
port[2]
