# @Author: wangyaominde  
# @Date: 2019-01-03 16:47:57  
# @Last Modified by:   wangyaominde  
# @Last Modified time: 2019-01-03 16:47:57
#%%
import serial.tools.list_ports


#%%
Com_Dict = {}  
#%%
port_list = list(serial.tools.list_ports.comports())
#%%
for port in port_list:
            Com_Dict["%s" % port[1]] = "%s" % port[1]