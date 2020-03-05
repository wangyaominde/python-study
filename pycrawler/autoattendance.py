# -*- coding: utf-8 -*-

import requests
#r = requests.get('http://ofweltoa.vicp.io:10880/login/Login.jsp', auth=('王耀民', 'RY7Mw7fEpUqTFt5'))

userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
header = {
    # "origin": "https://passport.mafengwo.cn",
    "Referer": "http://ofweltoa.vicp.io:10880/login/Login.jsp",
    'User-Agent': userAgent,
}

def attendancelogin(account, password):
    # 登录
    print ("开始模拟登录")

    postUrl = "http://ofweltoa.vicp.io:10880/login/VerifyLogin.jsp"
    postData = {
        "loginfile":"/wui/theme/ecology8/page/login.jsp?templateId=3&logintype=1&gopage= ",
        "logintype": "1" ,
        "fontName": "微软雅黑" ,
        "message":"",
        "gopage":"",
        "formmethod": "post" ,
        "rnd":"",
        "serial":"",
        "username":"",
        "isie": "false" ,
        "islanguid": "7" ,
        "loginid": account ,
        "userpassword": password ,
    }
    responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")

def attendanceout():
    requests.get("http://ofweltoa.vicp.io:10880/wui/theme/ecology7/page/getSystemTime.jsp?field=HH&token=1581879720268")

attendancelogin("王耀民","RY7Mw7fEpUqTFt5")
