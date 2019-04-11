# -*- coding: utf-8 -*-
import time
import xlrd
import xlwt
import os
import sys

file = input("请将要检测的excel文件拖入此对话框并且敲击回车").split("\"")[1]
print(os.path.abspath(file))

data = xlrd.open_workbook(str(os.path.abspath(file)))
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

i=0
print("参数不全：")
print("=========================================")
for c in range(1,ncols):
    if ('error-peak' in table.col_values(c) and table.col_values(c).count('error-peak')>3):
        i=i+1
        if(c%2==0):
            print(c/2)
        #print(table.col_values(c))
print("=========================================\n")

print("有：",int(100-i/2),"个可用")
os.system('pause')
