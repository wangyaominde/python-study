from datetime import datetime

try:
    time.sleep(0.5)
    print("hello world!")           #要执行的东西放在这
except Exception as e:              #除了错误就执行这里面的内容，把错误当作e
    now = datetime.now()            #获取当前时间用于记录
    f = open('Err_Log.txt', 'a')    #打开Err_Log.txt 并以追加的方式打开，用于查找之前的报错记录
    f.write(str(now)+'\0\0\0\0')    #将时间写入文件中
    f.write(str(e)+'\n')            #将错误信息写入文件中
else:                               #正常执行则运行如下内容
    print("success run")            
finally:                            #不论成功与否执行如下内容
    print("done")
