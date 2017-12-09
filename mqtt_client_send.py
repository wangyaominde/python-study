#-*-coding:utf-8-*-   
#基于mqtt的client程序，可以发送本机的ping百度的时间（时间没有分开，如果需要也可自己分离）
import paho.mqtt.client as mqtt    
import os
import time
client = mqtt.Client()
client.username_pw_set(username="#####", password="#####")
client.connect("104.207.158.9", 1883, 60)   
while 1:
	p=os.popen("ping -c1 www.baidu.com | awk '{print$8}' | grep 'time'")
	payload = p.read()
	print(payload)
	client.publish("ping", payload , qos=1, retain=False)
	time.sleep(300)
client.loop_forever() 
