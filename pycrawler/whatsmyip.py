import requests
from lxml import etree

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get(url='https://www.ip.cn',data=payload)
html=etree.HTML(r.text)
result=html.xpath('//*[@class="cf-footer-item"]/text()')

print(result[1][2:])