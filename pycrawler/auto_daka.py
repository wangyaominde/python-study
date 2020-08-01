import requests
from lxml import etree


payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.get(url='http://ofweltoa.vicp.io:10880/login/Login.jsp?gopage=&_token_=9fac2597-8468-4561-995a-f4778fb7bf13',data=payload)
html=etree.HTML(r.text)
result=html.xpath('//*[@class="txt"]/text()')

print(r.text)
