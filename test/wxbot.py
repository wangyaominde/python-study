import werobot
import autorasp

robot = werobot.WeRoBot(token='wangyaominde')

@robot.text
def echo(message):
    print(message.content)
    if(message.content in autorasp.autokey):
        return(autorasp.autokey[message.content])
    else:
        return("对不起，你说的我还不能理解")

@robot.image
def img(message):
    return("看不懂图片")

@robot.subscribe
def echo(message):
    return("呦，你来啦！")


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
