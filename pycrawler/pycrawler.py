import requests
from lxml import html

url='https://movie.douban.com/' #需要爬数据的网址
page=requests.Session().get(url)
tree=html.fromstring(page.text)
title_result=tree.xpath('//li//@data-title')
rate_result=tree.xpath('//li[@class="rating"]//span/text()')
title_result
rate_result

for i in range(len(title_result)):
    print(str(title_result[i])+":"+str(rate_result[i]))
