#edit by knva
#tool VSCODE
#time 2018-8-2 10:12:27
from wsgame import wsgame
from wsgamePlayer import wsgamePlayer
import threading
import time
import os
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
        wsg = wsgame(self.serverip, self.acctoken, self.player)
        wsg.start()

def run(serverurl, utoken, pid):
    wsg2 = MyThread(serverurl, utoken, pid)
    wsg2.start()

if __name__ == "__main__":
    mp.set_start_method('spawn')
    # 支持命令行 参数1 用户名 参数2 密码 参数3 区
    # 填服务器ip 默认1区
    myacc = os.environ["ACCOUNT"].split(' ')
    
    zone = myacc[2]
    username = myacc[0]
    password = myacc[1]
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
    accountMax = 5
    nowNum = 0
    for pid in userlist:
        # 参数1:服务器ip #参数2:用户accesstoken #参数3:pid  
        # 注意 若需要跳过某角色，请查询某角色id后， 输入  
        # if pid == 'xxxxxxxx': 
        #     continue
        if nowNum >= accountMax:
            break
        print("start")
        result = pp.apply_async(run,args=(serverurl, utoken, pid ,))
        tlist.append(result)
        nowNum = nowNum + 1
    pp.close()
    pp.join()

    print("操作结束")
