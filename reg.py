from wsgamereg import wsgame
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,serverip,acctoken,player="",sfname=""):
        super(MyThread, self).__init__()
        self.serverip=serverip
        self.acctoken =acctoken
    def run(self):
        wsg = wsgame(self.serverip,self.acctoken)
        wsg.start()

if __name__ == "__main__":
    #第一个参数是服务器id,第二个参数是用户登陆时的token,需要在浏览器抓,第三个是角色id ,第四个是,师门id
    #1武当 2少林 3华山 4峨眉 5逍遥 6丐帮
    wsg2= MyThread("ws://47.106.8.121:25631",
    "")
    wsg2.start()
