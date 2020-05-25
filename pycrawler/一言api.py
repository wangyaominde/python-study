# @Author: wangyaominde
# @Date: 2019-01-18 16:13:45
# @Last modified by:   wangyaominde
# @Last modified time: 2019-09-03T11:05:47+08:00

import json
import requests
#关闭https证书验证警告
requests.packages.urllib3.disable_warnings()
for i in range(5):
    r = requests.get(url="https://v1.hitokoto.cn/?c=h")
    a=r.json()
    print(a['hitokoto']+"---"+a['from'])
