# wsmud-game
武神传说日常脚本
# 本项目已经过时 推荐使用https://github.com/BenZinaDaze/wsdaily
---
运行需要安装websocket-client





配置说明:

*** 请不要输入中括号

```
pip install websocket-client==0.56.0

python demo.py [username] [password] [zone]

```

新增脚本用户控制从第x个角色到第y个角色的启动

```
python demo_select.py [username] [password] [zone] [start] [stop]

```

安卓使用termux 不支持pool 线程池,所以使用

```
python demo_termux.py [username] [password] [zone]
```

使用说明：

最近有很多人问如何使用本脚本

其实很简单，  本脚本基于python3.x  去官网下载安装python 3.x之后

访问以下链接将脚本下载下来。

https://github.com/knva/wsmud-game/archive/master.zip

解压缩后，用命令行进入文件夹

输入

```
pip install websocket-client
```

等待安装完毕后在输入

其中username 为用户名 password 为密码  zone为区服， 执行后就会自动执行帐号区服下所有的角色活跃任务

```
python demo.py [username] [password] [zone]
```

批量注册说明：

打开wsgamereg.py 找到最后一行，将账户 密码替换为自己需要注册角色的用户名即可  

批量注册如何选择区服：

![TIM截图20191016085919.png](https://i.loli.net/2019/10/16/WIfse6zSXYx8bhj.png)

打开浏览器 按F12找到network页面，将py脚本中的ip替换即可

![TIM截图20191016090028.png](https://i.loli.net/2019/10/16/FJ9RhcQmq3uw2fX.png)


脚本说明:

    运行流程

    1:登陆判断是否完成师门

    2:未完成,去买20个包子

    3:回到师门,刷到包子任务提交

    4:完成师门之后,刷副本, 副本为进入直接退出 ,需要修改的话,修改 wsgame.py中fuben以及richang函数

    5:每次刷完副本都会判断是否完成每日签到,完成则挖矿,否则继续副本
