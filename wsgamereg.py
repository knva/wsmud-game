#edit by knva
#tool VSCODE
#time 2018-8-2 10:12:27
import json
import os
import re
import threading
import time
import websocket
import sys
import urllib.request
import urllib.parse
from name import MkChineseName
from http import cookiejar
import json
try:
    import thread
except ImportError:
    import _thread as thread
import json
class wsgame:
    smflag = True
    yjdid = ''
    smid =''
    rc = False
    sfname = "薛慕华"
    sfid = ''
    dxename = "店小二"
    dxerid = ''
    tjname="铁匠"
    tjid =''
    zyzname="指引者"
    zyzid=''
    baoziname="包子"
    baoziid = ''
    tiegaoname="铁镐"
    tiegaoid=''
    mtiegaoid=''
    quanjiaoname ="拳脚快速入门"
    quanjiaoid=''
    neigongname="内功快速入门"
    neigongid=''
    mutourenname ="<hiw>木头人</hiw>"
    mutourenid=''
    mutourenstname ="<wht><hiw>木头人</hiw>的尸体</wht>"
    mutourenstid=''
    serverip=''
    acctoken = ''
    palyer =''
    smcode=1
    isReg =False
    action = {"n":'go north ',"s":'go south ',"w":'go west ',"e":'go east',"u":'go up',"d":'go down'}
    palyeraction = {"pack":'pack none',"nl":'dazuo',"ls":'liaoshang',"z":'zuo',"sx":'score',"edu":'study ',"set":'select ',"k":'kill ',"sq":'get all from ',"b":'buy ',"zb":'eq ',"qxzb":'uneq ',"wa":'wa'}
    wkaction=['jh fam 0 start','go west','go west','go west','go west','wa']
    fubenac=['jh fb 0 start1','cr cd/wen/damen','cr','cr over','taskover signin']
    maibaozi=['jh fam 0 start','go north','go north','go east','list'+ dxerid,'sell all','buy 20 '+ baoziid+" from "+ dxerid]
    xsrwaction= ['actions','select '+ zyzid,'guid '+ zyzid ,'zuo','zuo2 yizi','go east','pack','study '+ quanjiaoid,'next '+ zyzid,'go south','kill '+ mutourenid,'get all from '+ mutourenstid,'go north','next '+ zyzid,'pack none','study '+ neigongid,'liaoshang','next '+ zyzid,'ask6 '+ zyzid]
    maigao =['jh fam 0 start','go east','go east','go south','list '+ tjid,'buy 1 '+ tiegaoid+' from '+ tjid,'pack','eq '+ tiegaoid]
    def __init__(self, serverip, acctoken, palyer="",smcode=""):
      self.serverip = serverip
      self.acctoken=acctoken
      self.palyer = palyer
      self.smcode=smcode

    def convet_json(self,json_str):
        json_obj = eval(json_str, type('Dummy', (dict,), dict(__getitem__=lambda s,n:n))())
        return json_obj

    def xinshourenwu(self,ws):
        for ac in self.xsrwaction:
            print(ac)
            ws.send(ac)
            if ac == 'pack':
                time.sleep(1)
            if 'select' or 'guid' or 'next' or 'ask' in ac:
                ws.send(ac+self.zyzid)
            if 'study' in ac:
                ws.send(ac +self.quanjiaoid)
                ws.send(ac +self.neigongid)
                time.sleep(10)
            if 'kill' in ac:
                ws.send(ac +self.mutourenid)
                time.sleep(30)
            if 'get all from' in ac:
                ws.send(ac+self.mutourenstid)
            if 'liaoshang' in ac:
                time.sleep(5)
            time.sleep(2)
    def reg(self,ws):
        mk = MkChineseName()
        #ws.send()
        cc ="createrole "+mk.mkname()+" 1 15 15 20 30"
        print(cc)
        ws.send(cc)

    def saveUserId(self,ws,e):
        b = os.path.exists("user\\")
        if b:
            print('save')
        else:
            os.mkdir('user')

        fd = open( "user/users.json", 'r' )
        json_str = fd.read()
        fd.close()
        print(json_str)
        json_array = json.loads(json_str)
        json_array.append({"userid":e['id']})
        jsObj = json.dumps(json_array)
        print("保存账号"+e['id'])
        with open('user/users.json', "w") as fw:  
            fw.write(jsObj)  
            fw.close()

    def buytiegao(self,ws):
        
        print("tiegao")
        print(self.tjid)
        print(self.tiegaoid)
        for item in self.maigao:
            ws.send(item)
            time.sleep(1)
            if 'list' in item:
                time.sleep(1)
                ws.send("list "+self.tjid)
            if 'buy' in item:
                time.sleep(1)
                ws.send("buy 1 "+self.tiegaoid+" from "+self.tjid)
            if 'eq' in item:
                time.sleep(1)
                ws.send('eq '+self.mtiegaoid)

    def baishi(self,ws):
        self.baishia = ['jh fam 5 start','go north','go north','bai '+self.sfid]
        for item in self.baishia:
            ws.send(item)
            time.sleep(1)
            if 'bai' in item:
                ws.send(item+self.sfid)

    def sm(self,ws):
        ws.send("jh fam "+str(self.smcode)+" start")
        if self.smcode==1:
            self.sfname = "宋远桥"
            ws.send("go north")
        elif  self.smcode == 2:
            self.sfname = "清乐比丘"
        elif  self.smcode==3:
            self.sfname = "高根明"
        elif  self.smcode==4:
            self.sfname = "苏梦清"
            ws.send("go west")
        elif  self.smcode==5:
            self.sfname = "苏星河"
        elif  self.smcode==6:
            self.sfname = "左全"
            ws.send("go down")
        time.sleep(1)
        print(self.smflag)
        while self.smflag:
            time.sleep(1)
            ws.send("task sm "+self.smid)

    def baozi(self,ws):
        for ac in self.maibaozi:
            ws.send('ac')
            if 'list' in ac:
                time.sleep(1)
                ws.send("list "+self.dxerid)
            if 'buy' in ac:
                time.sleep(1)
                ws.send("buy 1 "+self.baoziid+" from "+self.dxerid)

    def richang(self,ws):
        if self.rc:
            return
        for ac in self.fubenac:
            ws.send(ac)
            time.sleep(0.5)

    def fuben(self,ws):
        for i in range(10):
            time.sleep(1)
            self.richang(ws)
        for i in range(5):
            time.sleep(1)
            if self.rc:
                return
            ws.send("use "+self.yjdid)
        for i in range(10):
            time.sleep(1)
            self.richang(ws)
            
            
    def wakuang(self,ws):
        for ac in self.wkaction:
            ws.send(ac)
            time.sleep(0.5)
        
    def lianxi(self,ws,e):
        if e['dialog']=='list':
            self.getitemsId(ws,e)
        if e['dialog']=="skills":
            print(e)
            print("技能 "+e['id'] +" 提升到 "+ str(e['exp'])+"%")
            if 'level' in e:
                #print(e)
                print("升级了"+"技能 "+e['id'] +"到"+str(e['level'])+"级")
        if self.yjdid =="":
            if e['dialog']=="pack":
                if 'items' in e:
                    for item in e['items']:
                        if self.yjdid=='':
                            if  "养精丹" in item['name']:
                                self.yjdid = item['id']
                                print("养精丹id:"+self.yjdid)
                                break
                        if self.tiegaoid=='':
                            if  self.tiegaoname in item['name']:
                                self.tiegaoid = item['id']
                                print("铁镐id:"+self.tiegaoid)
                                break
                        if self.quanjiaoid=='':
                            if  self.quanjiaoname in item['name']:
                                self.quanjiaoid = item['id']
                                print("拳脚id:"+self.quanjiaoid)
                                break
                if self.neigongid=='':
                    if  self.neigongname in e['name']:
                                self.neigongid = e['id']
                                print("内功id:"+self.neigongid)
                if self.mtiegaoid=='':
                    if  self.tiegaoname in item['name']:
                        self.mtiegaoid = item['id']
                        print("铁镐id:"+self.mtiegaoid)
                        
                             
    def getsmid(self,ws ,e):
        if 'items' in e:
            for item in e["items"]:
                #print(item)
                if item==0:
                    continue
                if self.smid =='':
                    if self.sfname in item["name"]:
                        self.smid = item['id']
                        self.sfid = item['id']
                        print("师门id:"+self.smid)
                        break
                if self.dxename in item["name"]:
                    self.dxerid = item['id']
                    print("店小二id:"+self.dxerid)
                    break
                if self.zyzid =='':
                    if self.zyzname in item["name"]:
                        self.zyzid = item['id']
                        print("指引者id:"+self.zyzid)
                        break
                if self.tjid =='':
                    if self.tjname in item["name"]:
                        self.tjid = item['id']
                        print("铁匠id:"+self.tjid)
                        break
    def getmtrid(self,ws,e):
        if self.mutourenid =='':
           if self.mutourenname == e["name"]:
                self.mutourenid = e['id']
                print("木头人id:"+self.mutourenid)
                    
        if self.mutourenstid =='':
            if self.mutourenstname == e["name"]:
                self.mutourenstid = e['id']
                print("木头人尸体id:"+self.mutourenstid)
    
    def saveStatic(self,ws,e):
        if '新手-训练室' in e['name']:
            self.isReg=True
    def getitemsId(self,ws,e):
        if self.dxerid == '':
            return
        if 'seller' in e:
            print("购买")
            if e['seller'] == self.dxerid:
                print("购买")
                for sellitem in e['selllist']:
                    if sellitem ==0:
                        continue
                    if self.baoziid =="":
                        if "包子" in sellitem['name']:
                            self.baoziid =sellitem['id']
                            print("包子id:"+self.baoziid)
                            break
            if e['seller'] == self.tjid:
                print("购买")
                for sellitem in e['selllist']:
                    if sellitem ==0:
                        continue                
                    if self.tiegaoid =="":
                        if self.tiegaoname in sellitem['name']:
                            self.tiegaoid =sellitem['id']
                            print("铁镐id:"+self.tiegaoid)
                            break
                    
    def smcmd(self,ws,e):
        print(e['items'][0]['cmd'])
        ws.send(e['items'][0]['cmd'])
        
    def on_message(self, message):
        if "{" and "}" in message: 
            e = self.convet_json(message)
            if e['type']=="dialog":
                self.lianxi(self.ws,e)
            if e['type']=="cmds":
                self.smcmd(self.ws,e)
            if e['type']=="items":
                self.getsmid(self.ws,e)
            if e['type']=="itemadd":
                self.getmtrid(self.ws,e)
            if e['type']=="room":
                self.saveStatic(self.ws,e)
        else:
            print(message)
            if "你今天已经签到了" in message:
                self.rc = True
            if "休息一下吧" in message:
                self.smflag = False
                
                
    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self,ws):
        def run(*args):
            time.sleep(1)
            ws.send(self.acctoken)
            # ws.send("login "+self.palyer)
            # time.sleep(1)
            # ws.send("stopstate")
            # ws.send('pack')
            # ws.send("taskover signin")
            # time.sleep(1)
            # ws.send("stopstate")
            # ws.send('pack')
            # ws.send("taskover signin")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            # print(self.rc)
            # if not self.rc:
            #     self.baozi(ws)
            #     self.sm(ws)
            #     self.fuben(ws)
            # self.wakuang(ws)
            self.reg(ws)
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            self.xinshourenwu(ws)
            time.sleep(1)
            self.buytiegao(ws)
            time.sleep(1)
            self.baishi(ws)
            #self.wakuang(ws)
            self.wakuang(ws)
            #ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, ())

    def start(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.serverip,
                                on_message = self.on_message,
                                  on_error = self.on_error,
                                  on_close = self.on_close)
        self.ws.on_open = self.on_open(self.ws)
        self.ws.run_forever()



class MyThread(threading.Thread):
    def __init__(self,serverip,acctoken,player="",sfname=""):
        super(MyThread, self).__init__()
        self.serverip=serverip
        self.acctoken =acctoken
    def run(self):
        wsg = wsgame(self.serverip,self.acctoken)
        wsg.start()
###
###获得登陆token
class GetLoginCookie:
    u=''
    p=''
    def __init__(self,username,password):
        self.username = username
        self.password =password
        self.post()
    def getCookie(self):
        return self.u +' '+self.p
    def post(self):
        cookie = cookiejar.CookieJar()
        post_url='http://game.wsmud.com/UserAPI/Login'
        handler = urllib.request.HTTPCookieProcessor(cookie) #创建cookie处理对象
        opener = urllib.request.build_opener(handler) #构建携带cookie的打开方式
        data = {'code':self.username,'pwd':self.password}
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(post_url,data,method = 'POST') #创建请求
        html = opener.open(req).read() #开启请求,保存登录cookie
        for item in cookie:
            if(item.name=='p'):
                self.p=item.value
            if(item.name=='u'):
                self.u=item.value
if __name__ == "__main__":

    c = GetLoginCookie('xxxxxxx','xxxxxxx')
    for i in range(5):
        wsg= MyThread("ws://120.79.75.160:25631/",c.getCookie())
        wsg.start()
        time.sleep(5)
    time.sleep(100000)