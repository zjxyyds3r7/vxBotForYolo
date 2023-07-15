import itchat
from itchat.content import *
import os
import yoloForBot

@itchat.msg_register([PICTURE])
def fun(msg):
    path = os.path.join('pic', msg.fileName)
    msg.download(path) # 下载图片
    res = yoloForBot.getResult(path)
    msg.user.send_image(os.path.join(res, msg.fileName))


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run(True)


