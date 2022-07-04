#edit by knva
#tool VSCODE
#time 2018-8-2 10:12:27
from wsgame import wsgame
from wsgamePlayer import wsgamePlayer
import threading
import time
from wsgameLogin import  GetLoginInfo
import sys
from multiprocessing import Process,Pool
import multiprocessing as mp

class MyThread(threading.Thread):
    def __init__(self, serverip, acctoken, player):
        super(MyThread, self).__init__()
        self.serverip = serverip
        self.acctoken = acctoken
        self.player = player
    def run(self):
        self.wsg = wsgame(self.serverip, self.acctoken, self.player)
        self.wsg.start()

def run(serverurl, utoken, pid):
    MyThread(serverurl, utoken, pid).start()

if __name__ == "__main__":
    mp.set_start_method('spawn')
    # 支持命令行 参数1 用户名 参数2 密码 参数3 区
    # 填服务器ip 默认1区
    zone = '1'
    username = ''
    password = ''
    # 默认启动第1个到第5个角色
    startaccount = 1
    stopaccount = 5
    if len(sys.argv) ==6:
        username = sys.argv[1]
        password = sys.argv[2]
        zone =  sys.argv[3]
        startaccount =  sys.argv[4]
        stopaccount =  sys.argv[5]
    # 参数1:用户名
    # 参数2:密码
    c = GetLoginInfo(username, password)
    c.getServer()
    utoken = c.getCookie()
    serverurl = c.getServerUrl(zone)
    print(serverurl)
    if utoken== ' ':
        print('账号密码错误')
        exit(0)
    else:
        print('Login success')
    # 参数1:服务器url
    # 参数2:用户accesstoken
    wsp = wsgamePlayer(serverurl, utoken)

    wsp.start()
    while (wsp.getStatic()):
        time.sleep(1)
    userlist = wsp.getList()
    pp = Pool()
    tlist = []

    nowNum = 1
    for pid in userlist:
        # 参数1:服务器ip #参数2:用户accesstoken #参数3:pid  
        # 注意 若需要跳过某角色，请查询某角色id后， 输入  
        # if pid == 'xxxxxxxx': 
        #     continue
        if nowNum >= int(startaccount) and nowNum <= int(stopaccount):
            print("start")
            result = pp.apply_async(run,args=(serverurl, utoken, pid ,))
            tlist.append(result)
        nowNum = nowNum + 1
    pp.close()
    pp.join()

    print("操作结束")
