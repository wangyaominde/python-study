'''for yy in range(2020,2051):
    for mm in range(1,13):
'''

import datetime
begin = datetime.date(2022,1,1)
end = datetime.date(2023,12,31)

for x in range(7):
    print(x+1)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        if(str(day)[5:7]==str(day)[8:10]):
            if(day.weekday()==x):
                print(str(day))
