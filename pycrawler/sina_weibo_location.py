import requests
from lxml import etree


payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get(url='https://s.weibo.com/weibo?q=*&region=custom:15:1&typeall=1&suball=1&Refer=SWeibo_box',data=payload)
html=etree.HTML(r.text)
result=html.xpath('//*[@class="txt"]/text()')

print(result)
