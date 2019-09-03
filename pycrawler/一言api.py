# @Author: wangyaominde
# @Date: 2019-01-18 16:13:45
# @Last modified by:   wangyaominde
# @Last modified time: 2019-09-03T11:01:30+08:00

import json
import requests
import re
#关闭https证书验证警告
requests.packages.urllib3.disable_warnings()
#url = "https://v1.hitokoto.cn/?c=d&encode=text"
#r = requests.get(url, verify=False)
#print(r.text)
r = requests.get(url="https://v1.hitokoto.cn/")
a=r.json()
print(a['hitokoto']+"---"+a['from'])
