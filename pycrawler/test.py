# -*- coding: UTF-8 -*-
# wangyaominde
# 2018.11.26 14:10
#

from urllib import request
import chardet

if __name__ == '__main__':
    response = request.urlopen("http://wthrcdn.etouch.cn/weather_mini?city=北京")
    html = response.read()
    # html = html.decode("utf-8") #use utfp decode
    charset = chardet.detect(html)  # auto decode
    html = html.decode(charset['encoding'])
    print(html)
