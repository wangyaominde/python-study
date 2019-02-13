# @Author: wangyaominde  
# @Date: 2019-01-18 15:41:50  
# @Last Modified by:   wangyaominde  
# @Last Modified time: 2019-01-18 15:41:50

import requests
import re
#关闭https证书验证警告
requests.packages.urllib3.disable_warnings()
# 12306的城市名和城市代码js文件url
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
r = requests.get(url, verify=False)
pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
result = re.findall(pattern, r.text)
station = dict(result)
print(station)
