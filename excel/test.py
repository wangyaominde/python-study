# -*- coding: utf-8 -*-
import time
import xlrd
import xlwt
import os
import sys

print(os.path.abspath('20181204162827-9.xls'))

data = xlrd.open_workbook('20181204162827-9.xls')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

for c in range(1,ncols):
    if ('error-peak' in table.col_values(c) and table.col_values(c).count('error-peak')>3):
        if(c%2==0):
            print(c/2)
        #print(table.col_values(c))
