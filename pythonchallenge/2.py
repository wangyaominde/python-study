# @Author: wangyaominde
# @Date:   2019-09-03T14:47:15+08:00
# @Last modified by:   wangyaominde
# @Last modified time: 2019-09-05T17:17:17+08:00

import requests
import re
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
r = requests.get(url)
result = r.text
re_comment = re.compile('<!--[^>]*-->')
result_content = re_comment.findall(result)
data=result_content[1]
resoult={}
for i in data:
    resoult[i]=data.count(i)

print(resoult)
