f = open(r"C:\ICS\config.ini", "w+", encoding="utf-8")
a = f.readlines()
dev = input("输入设备编号:\n")
for i in range(len(a)):
    if("DEVID=" in a[i]):
        a[i] = "DEVID="+dev+"\n"
        print(a[i])
    if("BANKNO=" in a[i]):
        a[i] = "BANKNO="+dev[0:4]+"\n"
        print(a[i])
