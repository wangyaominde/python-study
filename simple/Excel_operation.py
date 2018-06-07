# -*- coding: utf-8 -*-
import xlrd
from xpinyin import  Pinyin

p = Pinyin()
f = open('a.txt','w')
f.write("{\n  \"ips\": [")

data = xlrd.open_workbook("a.xlsx")
table = data.sheet_by_name(u'Sheet1')
print(data.sheet_names())
print (table.name,table.nrows,table.ncols)
for i in range (table.nrows):
    f.write("\n")
    rows = table.row_values(i)
    rows[1]=p.get_pinyin(rows[1],"")
    f.write("     {\n")
    f.write("\t\"name\": \""+rows[1]+"_"+rows[2]+"\",\n")
    f.write("\t\"dev\": \"\",\n")
    if (i == table.nrows):
        f.write("\t\"ip\": \""+rows[0]+"\"\n     }")
    else :
        f.write("\t\"ip\": \""+rows[0]+"\"\n     },")
    print(rows)
f.write("\n  ]\n}")