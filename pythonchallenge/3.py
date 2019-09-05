# @Author: wangyaominde
# @Date:   2019-09-05T17:17:31+08:00
# @Last modified by:   wangyaominde
# @Last modified time: 2019-09-05T17:25:41+08:00

import requests
import re
url = "http://www.pythonchallenge.com/pc/def/equality.html"
r = requests.get(url)
result = r.text
re_comment = re.compile('<!--[^>]*-->')
result_content = re.findall("[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}",result)
for i in range(len(result_content)):
    print(result_content[i][4])
