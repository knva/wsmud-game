# edit by knva
# tool VSCODE
# time 2018-8-2 10:12:27
import threading
import websocket

from wsgamePlayer import wsgamePlayer

try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import re

class wsgame:
    smflag = True
    running = True
    yjdid = ''
    lvyjdid= ''
    goldlow = False
    smid = ''
    rc = False
    ym = False
    sfname = "苏星河"
    sxid = ''
    mp = ''
    dxerid = ''
    dxename = "店小二"
    baoziid = ''
    serverip = ''
    acctoken = ''
    palyer = ''
    smcode = 1
    die = False
    myname = ''
    zbid = ''
    smgood =''
    smbreak = False
    sdf = 0
    tiegao = ''
    addr = {"住房": "jh fam 0 start;go west;go west;go north;go enter",
            "住房-卧室": "jh fam 0 start;go west;go west;go north;go enter;go north",
            "住房-小花园": "jh fam 0 start;go west;go west;go north;go enter;go northeast",
            "住房-炼药房": "jh fam 0 start;go west;go west;go north;go enter;go southwest",
            "住房-练功房": "jh fam 0 start;go west;go west;go north;go enter;go west",
            "扬州城-钱庄": "jh fam 0 start;go north;go west;store",
            "扬州城-广场": "jh fam 0 start",
            "扬州城-醉仙楼": "jh fam 0 start;go north;go north;go east",
            "扬州城-杂货铺": "jh fam 0 start;go east;go south",
            "扬州城-打铁铺": "jh fam 0 start;go east;go east;go south",
            "扬州城-药铺": "jh fam 0 start;go east;go east;go north",
            "扬州城-衙门正厅": "jh fam 0 start;go west;go north;go north",
            "扬州城-镖局正厅": "jh fam 0 start;go west;go west;go south;go south",
            "扬州城-矿山": "jh fam 0 start;go west;go west;go west;go west",
            "扬州城-喜宴": "jh fam 0 start;go north;go north;go east;go up",
            "扬州城-擂台": "jh fam 0 start;go west;go south",
            "扬州城-当铺": "jh fam 0 start;go south;go east",
            "扬州城-帮派": "jh fam 0 start;go south;go south;go east",
            "帮会-大门": "jh fam 0 start;go south;go south;go east;go east",
            "帮会-大院": "jh fam 0 start;go south;go south;go east;go east;go east",
            "帮会-练功房": "jh fam 0 start;go south;go south;go east;go east;go east;go north",
            "帮会-聚义堂": "jh fam 0 start;go south;go south;go east;go east;go east;go east",
            "帮会-仓库": "jh fam 0 start;go south;go south;go east;go east;go east;go east;go north",
            "帮会-炼药房": "jh fam 0 start;go south;go south;go east;go east;go east;go south",
            "扬州城-扬州武馆": "jh fam 0 start;go south;go south;go west",
            "扬州城-武庙": "jh fam 0 start;go north;go north;go west",
            "武当派-广场": "jh fam 1 start;",
            "武当派-三清殿": "jh fam 1 start;go north",
            "武当派-石阶": "jh fam 1 start;go west",
            "武当派-练功房": "jh fam 1 start;go west;go west",
            "武当派-太子岩": "jh fam 1 start;go west;go northup",
            "武当派-桃园小路": "jh fam 1 start;go west;go northup;go north",
            "武当派-舍身崖": "jh fam 1 start;go west;go northup;go north;go east",
            "武当派-南岩峰": "jh fam 1 start;go west;go northup;go north;go west",
            "武当派-乌鸦岭": "jh fam 1 start;go west;go northup;go north;go west;go northup",
            "武当派-五老峰": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup",
            "武当派-虎头岩": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup",
            "武当派-朝天宫": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north",
            "武当派-三天门": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north",
            "武当派-紫金城": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north",
            "武当派-林间小径": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north;go north;go north",
            "武当派-后山小院": "jh fam 1 start;go west;go northup;go north;go west;go northup;go northup;go northup;go north;go north;go north;go north;go north;go north",
            "少林派-广场": "jh fam 2 start;",
            "少林派-山门殿": "jh fam 2 start;go north",
            "少林派-东侧殿": "jh fam 2 start;go north;go east",
            "少林派-西侧殿": "jh fam 2 start;go north;go west",
            "少林派-天王殿": "jh fam 2 start;go north;go north",
            "少林派-大雄宝殿": "jh fam 2 start;go north;go north;go northup",
            "少林派-钟楼": "jh fam 2 start;go north;go north;go northeast",
            "少林派-鼓楼": "jh fam 2 start;go north;go north;go northwest",
            "少林派-后殿": "jh fam 2 start;go north;go north;go northwest;go northeast",
            "少林派-练武场": "jh fam 2 start;go north;go north;go northwest;go northeast;go north",
            "少林派-罗汉堂": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go east",
            "少林派-般若堂": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go west",
            "少林派-方丈楼": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north",
            "少林派-戒律院": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go east",
            "少林派-达摩院": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go west",
            "少林派-竹林": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north",
            "少林派-藏经阁": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go west",
            "少林派-达摩洞": "jh fam 2 start;go north;go north;go northwest;go northeast;go north;go north;go north;go north;go north",
            "华山派-镇岳宫": "jh fam 3 start;",
            "华山派-苍龙岭": "jh fam 3 start;go eastup",
            "华山派-舍身崖": "jh fam 3 start;go eastup;go southup",
            "华山派-峭壁": "jh fam 3 start;go eastup;go southup;jumpdown",
            "华山派-山谷": "jh fam 3 start;go eastup;go southup;jumpdown;go southup",
            "华山派-山间平地": "jh fam 3 start;go eastup;go southup;jumpdown;go southup;go south",
            "华山派-林间小屋": "jh fam 3 start;go eastup;go southup;jumpdown;go southup;go south;go east",
            "华山派-玉女峰": "jh fam 3 start;go westup",
            "华山派-玉女祠": "jh fam 3 start;go westup;go west",
            "华山派-练武场": "jh fam 3 start;go westup;go north",
            "华山派-练功房": "jh fam 3 start;go westup;go north;go east",
            "华山派-客厅": "jh fam 3 start;go westup;go north;go north",
            "华山派-偏厅": "jh fam 3 start;go westup;go north;go north;go east",
            "华山派-寝室": "jh fam 3 start;go westup;go north;go north;go north",
            "华山派-玉女峰山路": "jh fam 3 start;go westup;go south",
            "华山派-玉女峰小径": "jh fam 3 start;go westup;go south;go southup",
            "华山派-思过崖": "jh fam 3 start;go westup;go south;go southup;go southup",
            "华山派-山洞": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter",
            "华山派-长空栈道": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup",
            "华山派-落雁峰": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup;go westup",
            "华山派-华山绝顶": "jh fam 3 start;go westup;go south;go southup;go southup;break bi;go enter;go westup;go westup;jumpup",
            "峨眉派-金顶": "jh fam 4 start",
            "峨眉派-庙门": "jh fam 4 start;go west",
            "峨眉派-广场": "jh fam 4 start;go west;go south",
            "峨眉派-走廊": "jh fam 4 start;go west;go south;go west",
            "峨眉派-休息室": "jh fam 4 start;go west;go south;go east;go south",
            "峨眉派-厨房": "jh fam 4 start;go west;go south;go east;go east",
            "峨眉派-练功房": "jh fam 4 start;go west;go south;go west;go west",
            "峨眉派-小屋": "jh fam 4 start;go west;go south;go west;go north;go north",
            "峨眉派-清修洞": "jh fam 4 start;go west;go south;go west;go south;go south",
            "峨眉派-大殿": "jh fam 4 start;go west;go south;go south",
            "峨眉派-睹光台": "jh fam 4 start;go northup",
            "峨眉派-华藏庵": "jh fam 4 start;go northup;go east",
            "逍遥派-青草坪": "jh fam 5 start",
            "逍遥派-林间小道": "jh fam 5 start;go east",
            "逍遥派-练功房": "jh fam 5 start;go east;go north",
            "逍遥派-木板路": "jh fam 5 start;go east;go south",
            "逍遥派-工匠屋": "jh fam 5 start;go east;go south;go south",
            "逍遥派-休息室": "jh fam 5 start;go west;go south",
            "逍遥派-木屋": "jh fam 5 start;go north;go north",
            "逍遥派-地下石室": "jh fam 5 start;go down;go down",
            "丐帮-树洞内部": "jh fam 6 start",
            "丐帮-树洞下": "jh fam 6 start;go down",
            "丐帮-暗道": "jh fam 6 start;go down;go east",
            "丐帮-破庙密室": "jh fam 6 start;go down;go east;go east;go east",
            "丐帮-土地庙": "jh fam 6 start;go down;go east;go east;go east;go up",
            "丐帮-林间小屋": "jh fam 6 start;go down;go east;go east;go east;go east;go east;go up",
            "杀手楼-大门": "jh fam 7 start",
            "杀手楼-大厅": "jh fam 7 start;go north",
            "杀手楼-暗阁": "jh fam 7 start;go north;go up",
            "杀手楼-铜楼": "jh fam 7 start;go north;go up;go up",
            "杀手楼-休息室": "jh fam 7 start;go north;go up;go up;go east",
            "杀手楼-银楼": "jh fam 7 start;go north;go up;go up;go up;go up",
            "杀手楼-练功房": "jh fam 7 start;go north;go up;go up;go up;go up;go east",
            "杀手楼-金楼": "jh fam 7 start;go north;go up;go up;go up;go up;go up;go up",
            "杀手楼-书房": "jh fam 7 start;go north;go up;go up;go up;go up;go up;go up;go west",
            "杀手楼-平台": "jh fam 7 start;go north;go up;go up;go up;go up;go up;go up;go up",
            "襄阳城-广场": "jh fam 8 start",
            "武道塔": "jh fam 9 start"
            }
    sm_array = {
        '武当派': {
            'place': "武当派-三清殿",
            'npc': "武当派第二代弟子 武当首侠 宋远桥",
            'sxplace': "武当派-太子岩",
            'sx': "首席弟子"
        },
        '华山派': {
            'place': "华山派-镇岳宫",
            'npc': "市井豪杰 高根明",
            'sxplace': "华山派-练武场",
            'sx': "首席弟子"
        },
        '少林派': {
            'place': "少林派-天王殿",
            'npc': "少林寺第三十九代弟子 道觉禅师",
            'sxplace': "少林派-练武场",
            'sx': "大师兄"
        },
        '逍遥派': {
            'place': "逍遥派-青草坪",
            'npc': "聪辩老人 苏星河",
            'sxplace': "-jh fam 5 start;go west",
            'sx': "首席弟子"
        },
        '丐帮': {
            'place': "丐帮-树洞下",
            'npc': "丐帮七袋弟子 左全",
            'sxplace': "丐帮-破庙密室",
            'sx': "首席弟子"
        },
        '峨眉派': {
            'place': "峨眉派-大殿",
            'npc': "峨眉派第四代弟子 静心",
            'sxplace': "峨眉派-广场",
            'sx': "大师姐"
        },
        '无门无派': {
            'place': "扬州城-扬州武馆",
            'npc': "武馆教习",
            'sxplace': "扬州城-扬州武馆"
        },
        '杀手楼': {
            'place': "杀手楼-大厅",
            'npc': "杀手教习 何小二",
            'sxplace': "杀手楼-练功房",
            'sx': "金牌杀手"
        }
    }
    goods = {
        "<wht>米饭</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>包子</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>鸡腿</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>面条</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>扬州炒饭</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>米酒</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>花雕酒</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>女儿红</wht>": {
            "id": None,
            "type": "wht",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<hig>醉仙酿</hig>": {
            "id": None,
            "type": "hig",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<hiy>神仙醉</hiy>": {
            "id": None,
            "type": "hiy",
            "sales": "店小二",
            "place": "扬州城-醉仙楼"
        },
        "<wht>布衣</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>钢刀</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>木棍</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>英雄巾</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>布鞋</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>铁戒指</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>簪子</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>长鞭</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>钓鱼竿</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>鱼饵</wht>": {
            "id": None,
            "type": "wht",
            "sales": "杂货铺老板 杨永福",
            "place": "扬州城-杂货铺"
        },
        "<wht>铁剑</wht>": {
            "id": None,
            "type": "wht",
            "sales": "铁匠铺老板 铁匠",
            "place": "扬州城-打铁铺"
        },
        "<wht>钢刀</wht>": {
            "id": None,
            "type": "wht",
            "sales": "铁匠铺老板 铁匠",
            "place": "扬州城-打铁铺"
        },
        "<wht>铁棍</wht>": {
            "id": None,
            "type": "wht",
            "sales": "铁匠铺老板 铁匠",
            "place": "扬州城-打铁铺"
        },
        "<wht>铁杖</wht>": {
            "id": None,
            "type": "wht",
            "sales": "铁匠铺老板 铁匠",
            "place": "扬州城-打铁铺"
        },
        "<wht>铁镐</wht>": {
            "id": None,
            "type": "wht",
            "sales": "铁匠铺老板 铁匠",
            "place": "扬州城-打铁铺"
        },
        "<wht>飞镖</wht>": {
            "id": None,
            "type": "wht",
            "sales": "铁匠铺老板 铁匠",
            "place": "扬州城-打铁铺"
        },
        "<hig>金创药</hig>": {
            "id": None,
            "type": "hig",
            "sales": "药铺老板 平一指",
            "place": "扬州城-药铺"
        },
        "<hig>引气丹</hig>": {
            "id": None,
            "type": "hig",
            "sales": "药铺老板 平一指",
            "place": "扬州城-药铺"
        },
          "<hic>金创药</hic>": {
            "id": None,
            "type": "hic",
            "sales": "药铺老板 平一指",
            "place": "扬州城-药铺"
        },
        "<hic>引气丹</hic>": {
            "id": None,
            "type": "hic",
            "sales": "药铺老板 平一指",
            "place": "扬州城-药铺"
        },
        "<hig>养精丹</hig>": {
            "id": None,
            "type": "hig",
            "sales": "药铺老板 平一指",
            "place": "扬州城-药铺"
        }
    }
    yb = 0
    bagsize = 0
    bagitemsize = 0
    bagshitou = ''
    autouse = None
    npcs={ "店小二": 0, "铁匠铺老板 铁匠": 0, "药铺老板 平一指": 0, "杂货铺老板 杨永福": 0 ,"扬州知府 程药发":0}
    npcsj = ''
    name =''
    def __init__(self, serverip, acctoken, palyer="",name=''):
        self.serverip = serverip
        self.acctoken = acctoken
        self.palyer = palyer
        if name =='':
            self.name = time.strftime('%H%M%S',time.localtime(time.time()))
        else:
            self.name = name
    def getrun(self):
        return self.running

    def sendcmd(self, cmd):
        cmd = cmd.split(";")
        for i in cmd:
            if '$' in i:
                i.replace('$', '')
                parg = i.split(" ")[1]
                if 'wait' in i:
                    time.sleep(int(parg) / 1000)
            else:
                #print('send:'+i)
                self.ws.send(i)

    def convet_json(self, json_str):
        json_obj = eval(json_str, type('Dummy', (dict,), dict(__getitem__=lambda s, n: n))())
        return json_obj

    def logCat(self, msg):
        print("{0}: {1}: {2}".format(time.strftime('%H:%M:%S',time.localtime(time.time())), self.myname, msg))

    def go(self, addr):
        if self.addr[addr] is not None:
            self.sendcmd( self.addr[addr])

    def sm(self):
        while self.mp == '':
            time.sleep(1)
        self.go( self.sm_array[self.mp]['place'])
        self.sfname = self.sm_array[self.mp]['npc']
        time.sleep(1)
        self.logCat(self.smflag)
        while self.smflag:
            time.sleep(1)
            self.sendcmd("task sm " + self.smid)
            time.sleep(0.5)
            while self.smgood == '' and  (not self.smbreak):
                self.go(self.sm_array[self.mp]['place'])
                time.sleep(1)
                self.sendcmd("task sm " + self.smid)
                time.sleep(0.5)
            if self.smbreak:
                self.smbreak =False
                continue;
            if self.smgood in self.goods.keys():
                self.go(self.goods[self.smgood]['place'])
                time.sleep(1)
                if self.smbreak:
                    self.smbreak = False
                    continue;
                self.logCat("需要购买:" + self.smgood)
                self.sendcmd('list {0}'.format(self.npcs[self.goods[self.smgood]['sales']]))
                time.sleep(0.2)
                self.sendcmd('buy 1 {0} from {1}'.format(self.goods[self.smgood]['id'],self.npcs[self.goods[self.smgood]['sales']]))
                time.sleep(0.1)
                self.go( self.sm_array[self.mp]['place'])
                time.sleep(2)
            else:
                self.sendcmd("task sm " + self.smid+" giveup")
                self.logCat("task sm " + self.smid+" giveup")
                self.logCat("无法购买:"+self.smgood)
                self.smgood=''
                time.sleep(1)

    def baozi(self):
        self.go( '扬州城-醉仙楼')
        time.sleep(1)
        self.sendcmd('sell all')
        self.go( '扬州城-杂货铺')
        time.sleep(1)
        self.go( '扬州城-打铁铺')
        time.sleep(1)
        self.go('扬州城-药铺')
        time.sleep(1)

    def richang(self):
        if self.rc:
            return
        time.sleep(1)
        self.sendcmd("jh fb 0 start1;cr yz/lw/shangu;cr over")
        self.sendcmd("taskover signin")

    def fuben(self):
        self.sendcmd('pack')
        time.sleep(5)
        for i in range(10):
            time.sleep(0.5)
            self.richang()
        for i in range(5):
            time.sleep(1)
            if self.rc:
                return
            self.sendcmd("use " + self.yjdid)
        for i in range(10):
            time.sleep(1)
            self.richang()

    def zhuibu(self):
        self.go( '扬州城-衙门正厅')
        while self.npcs['扬州知府 程药发']== 0:
            time.sleep(1)
        self.sendcmd('ask1 ' + self.npcs['扬州知府 程药发'])
        time.sleep(1)
        self.sendcmd('ask2 ' + self.npcs['扬州知府 程药发'])
        time.sleep(1)
        self.sendcmd('pack')
        time.sleep(2)
        if self.sdf < 20:
            self.logCat('购入需要的扫荡符{0}'.format(20 - self.sdf))
            self.sendcmd('shop 0 {0}'.format(20 - self.sdf))
        self.sendcmd('ask3 ' + self.npcs['扬州知府 程药发'])

    def wakuang(self):
        self.sendcmd('pack')
        time.sleep(1)
        #self.go( "扬州城-矿山")
        #time.sleep(1)
        if self.tiegao == '':
            self.go( "扬州城-打铁铺")
            time.sleep(1)
            self.sendcmd("list {0}".format(self.npcs[self.goods['<wht>铁镐</wht>']['sales']]))
            time.sleep(1)
            self.sendcmd("buy 1 {0} from {1}".format(self.goods['<wht>铁镐</wht>']['id'],self.npcs[self.goods['<wht>铁镐</wht>']['sales']]))
            self.wakuang()
        else:
            self.sendcmd("$wait 1000;$to 住房-练功房;dazuo")
            #self.sendcmd("eq {0};wa".format(self.tiegao))

    def lianxi(self, e):
        if e['dialog'] =='shop':
            self.yb = e['cash_money']
        if e['dialog'] == 'list':
            self.getitemsId( e)
        if e['dialog'] == "skills":
            self.logCat("技能 " + e['id'] + " 提升到 " + str(e['exp']) + "%")
            if 'level' in e:
                # self.logCat(e)
                self.logCat("升级了" + "技能 " + e['id'] + "到" + str(e['level']) + "级")
        if e['dialog'] == "pack":
            if 'items' in e:
                self.bagsize = e['max_item_count']
                self.bagitemsize = len(e['items'])
                for item in e['items']:
                    #self.logCat(item)
                    if "<hic>养精丹</hic>" in item['name']:
                        self.yjdid = item['id']
                        #self.logCat("养精丹id:" + self.yjdid)
                    if "扫荡符" in item['name']:
                        self.sdf = item['count']
                        #self.logCat("扫荡符数量:{0}".format (self.sdf))
                    if "铁镐" in item['name']:
                        self.tiegao = item['id']
                        #self.logCat("铁镐id:{0}".format (self.tiegao))
                    if "<hig>养精丹</hig>" in item['name']:
                        self.lvyjdid = item['id']

            if 'eqs' in e:
                for item in e['eqs']:
                    if 'name'in item.keys() and "铁镐" in item['name']:
                        self.tiegao = item['id']
                        #elf.logCat("铁镐id:{0}".format (self.tiegao))
            if 'name' in e:
                if "背包扩充石" in e['name']:
                    self.bagshitou =  e['id']

        if self.mp == '':
            if e['dialog'] == 'score':
                self.mp = e['family']
        if e['dialog'] == 'tasks':
            if e['items'] != None:
                for item in e['items']:
                    if item['id'] == 'yamen':
                        if '20/20' in item['desc']:
                            self.ym = True
                            return
    def qa(self):
        while self.mp == '':
            time.sleep(1)
        if(self.mp=="无门无派"):
            return
        sxpath = self.sm_array[self.mp]['sxplace']
        
        time.sleep(1)
        print(sxpath)
        if sxpath[0]=='-':
            self.sendcmd( sxpath.replace("-",""))
        else:
            self.go(sxpath)
        while self.sxid =='':
            time.sleep(1)
        self.sendcmd("ask2 {0}".format(self.sxid))
        time.sleep(1)
        
    def yj(self):
        while self.lvyjdid=='':
            self.go(self.goods["<hig>养精丹</hig>"]['place'])
            time.sleep(1)
            self.sendcmd("list {0}".format(self.npcs[self.goods['<hig>养精丹</hig>']['sales']]))
            self.sendcmd('buy 10 {0} from {1}'.format(self.goods["<hig>养精丹</hig>"]['id'],self.npcs[self.goods["<hig>养精丹</hig>"]['sales']]))
            self.sendcmd("pack")
            time.sleep(1)
            if self.goldlow:
                return
        for i in range(10):
            self.sendcmd('use {0};$wait 500'.format(self.lvyjdid))

    def getsmid(self, e):
        if 'items' in e:
            for item in e["items"]:
                # self.logCat(item)
                if item == 0:
                    continue
                if self.smid == '':
                    if self.sfname in item["name"]:
                        self.smid = item['id']
                        self.logCat("师门id:" + self.smid)
                        break
                if item["name"] in self.npcs:
                    self.npcs[item["name"]] = item['id']
                    #self.logCat(self.npcs)
                    # self.npcsj = json.dumps(self.npcs)
                    break
                if self.sm_array[self.mp]['sx'] in item['name']:
                    self.sxid = item['id']


    def getitemsId(self, e):
        if 'seller' in e:
            for item in e['selllist']:
                if item['name'] in self.goods.keys():
                    self.goods[item['name']]['id']=item['id']
            #self.logCat(self.goods)

    def smcmd(self, e):
        if not self.smflag:
            return
        for item in e['items']:
            if item['name'] is None:
                break
            self.logCat(item['name'])
            if self.smgood in item['name']:
                self.sendcmd(item['cmd'])
                self.logCat('交任务物品')
                self.smgood = ''
                self.smbreak =True
                time.sleep(1)
                return

    def relive(self, e):
        self.sendcmd('relive')
        self.die = True

    def bagresize(self):
        if self.yb > 80 and self.bagsize<100:
            self.logCat("元宝充足,购买背包扩容")
            self.sendcmd('shop 2 1')
            time.sleep(1)
            self.sendcmd('use {0}'.format(self.bagshitou))
        else:
            self.logCat("无法购买背包扩容")

    def afterwards(self):
        self.logCat('使用可用物品开始')
        if self.palyer == '':
            self.logCat('使用可用物品结束')
            return
        self.autouse = self.au.getUseList(self.palyer)
        print("{0}:{1}".format(self.palyer, self.autouse))
        cmds = ''
        for item in self.autouse:
            for i in range(self.autouse[item]['count']):
                cmds+='use {0};$wait 500;'.format(self.autouse[item]['id'])
                self.logCat('使用{0}'.format(item))
        self.sendcmd(cmds)
        self.logCat('使用可用物品结束')

    def login(self):
        self.sendcmd(self.acctoken)
        self.sendcmd("login " + self.palyer)
        time.sleep(1)
        self.sendcmd('setting ban_pk 1')
        self.sendcmd('setting off_move 1')
        self.sendcmd("stopstate;tm knva")
        time.sleep(1)
        self.logCat("3")
        self.sendcmd('pack;taskover signin;shop')
        time.sleep(1)
        self.logCat("2")
        self.sendcmd('score;$wait 500;tasks')
        time.sleep(1)
        self.logCat("1")
        print('{0}:{1}'.format(self.name,self.npcsj))
        if self.myname == '':
            self.logCat("登录失败,重新登录")
            time.sleep(5)
            self.login()

    def getmyname(self, e):
        if e['ch'] == 'tm' and e['uid'] == self.palyer:
            self.myname = e['name']
            #print(self.myname)

    def on_message(self, message):
        if "{" and "}" in message:
            e = self.convet_json(message)
            #self.logCat(e)
            if e['type'] == "dialog":
                self.lianxi( e)
            if e['type'] == "cmds":
                self.smcmd( e)
            if e['type'] == "items":
                self.getsmid( e)
            if e['type'] == "msg":
                self.getmyname(e)
        else:
            if "你去帮我找一件" in message or "我要的是" in message or "你去帮我找一下吧" in message or '你去帮我找些' in message:
                res = re.findall(r'>(.*?)<', message)
                ptag = re.findall(r'<(.*?)>', message)
                self.smgood = "<{0}>{1}<{2}>".format(ptag[0],res[0],ptag[1])
            self.logCat(message)
            if "你今天已经签到了" in message:
                self.rc = True
            if "休息一下吧" in message:
                self.smflag = False
                self.smbreak=True
            if "灵魂状态" in message:
                self.relive( message)
            if '你没有那么多的钱' in message:
                self.goldlow = True
                self.rc = True

    def on_error(self, error):
        self.logCat(error)

    def on_close(self):
        self.logCat("### 断开连接 ###")

    def on_open(self):
        def run(*args):
            time.sleep(1)
            self.login()
            self.logCat("日常完成:{0}".format(self.rc))
            self.baozi()
            self.qa()
            #self.yj()
            while True:
                if not self.rc:
                    if (self.bagitemsize - self.bagsize) < 5:
                        self.bagresize()
                    else:
                        self.logCat("背包空间足够,无需扩容")
                    self.sm()
                    self.sendcmd("taskover signin")
                    self.sendcmd("taskover signin")
                    self.fuben()
                if not self.die:
                    break
            if not self.ym:
                self.zhuibu()
            self.ws.send('pack')
            self.wakuang()
            self.ws.close()
            self.logCat("线程结束")
            self.ws.close()
            self.running = False
        thread.start_new_thread(run, ())

    def start(self):

        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(self.serverip,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()
