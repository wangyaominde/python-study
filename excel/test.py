import time
import xlrd
import xlwt

data = xlrd.open_workbook('20181210013431-1.xls')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols

for c in range(1,ncols):
    print(table.col_values(c))


'''for r in range(3,nrows):
    for c in range(1,ncols):
        if(table.cell(r,c).value=='error-peak'):
            if(c%2==0):
                print(c/2)'''
