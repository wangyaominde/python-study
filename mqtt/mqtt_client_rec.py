#-*-coding:utf-8-*-
#基于mqtt的client程序，可以订阅消息
import paho.mqtt.client as mqtt

# 当连接上服务器后回调此函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#订阅主题")

# 从服务器接受到消息后回调此函数
def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload))
client = mqtt.Client()
#参数有 Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client.on_connect = on_connect #设置连接上服务器回调函数
client.on_message = on_message  #设置接收到服务器消息回调函数
client.username_pw_set(username="test", password="1472583690")
client.connect("#服务器地址", 1883, 60)   
client.loop_forever()
