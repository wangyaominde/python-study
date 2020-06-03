#-*-coding:utf-8-*-
import paho.mqtt.client as mqtt
import wol
import whatsmyip

#wol.send_magic_packet('2CF05D0851D8')#
# 当连接上服务器后回调此函数
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/wol")

# 从服务器接受到消息后回调此函数
def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload))
    if(msg.payload==b'wake on lan'):
        wol.send_magic_packet('2CF05D0851D8')
    if(msg.payload==b'get ip'):
        print(whatsmyip.getip())
        client.publish("/ip", whatsmyip.getip() , qos=1, retain=False) #对于ping订阅发送当前获取的延迟时间
        

client = mqtt.Client()
#参数有 Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
client.on_connect = on_connect #设置连接上服务器回调函数
client.on_message = on_message  #设置接收到服务器消息回调函数
client.connect("#服务器地址", 1883, 60)   
client.loop_forever()
