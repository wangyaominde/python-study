#code by wangyaomin

import itchat


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg['User']['NickName'])
    print(":")
    print(msg['Text'])
    print("\n\n")
    return ("您好，您发的留言我已经收到，我会在看到消息的第一时间回复您，谢谢！(auto response!)")

itchat.auto_login(enableCmdQR=2)   #命令行二维码
#itchat.auto_login(1)
itchat.run()
