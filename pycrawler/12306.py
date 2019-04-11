# @Author: wangyaominde  
# @Date: 2019-01-18 16:13:45  
# @Last Modified by:   wangyaominde  
# @Last Modified time: 2019-01-18 16:13:45


#%%
import requests
import re
#%%
#关闭https证书验证警告
requests.packages.urllib3.disable_warnings()
url = "https: // kyfw.12306.cn/otn/leftTicket/init?linktypeid = dc & fs =上海, SHH & ts = 北京, BJP & date = 2019-01-18 & flag = N, N, Y"
r = requests.get(url, verify=False)
print(r.text)
