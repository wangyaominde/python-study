#!/usr/bin/python
# -*- coding: utf-8 -*-
flag = 0
flag1 = 0
name = ''
pwd = 0


def inpnp():
    global name
    global pwd
    name = str(input())
    pwd = int(eval(input()))


def match(name, pwd):
    global flag1
    flag1 += 1
    if name == 'kate':
        if pwd == 666666:
            print('登录成功！')
            return 1
        else:
            global flag
            flag += 1
            print('用户名或者密码错误！')
    else:
        flag += 1
        print('用户名或者密码错误！')


while flag1 < 3:
    inpnp()
    if match(name, pwd) == 1:
        break
if flag1 == 3:
    print('3次用户名或者密码均有误！退出程序。')
