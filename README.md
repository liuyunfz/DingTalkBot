# DingTalkBot
代码可用性： ![DingTalk_misson](https://github.com/liuyunfz/DingTalkBot/workflows/DingTalk_misson/badge.svg)
## 这是什么
基于python写的钉钉机器人，通过GitHub Action定时任务实现自动化。
## 有什么用
可以零成本创建属于自己的钉钉机器人，定时推送订阅内容（例如优惠消息等线报亦或是喜欢UP主的更新）；而且完全基于GitHub，也就是说你不需要了解任何编程知识，只需要按照教程稍微部署一下即可获得一个属于自己的钉钉机器人。
## 如何使用
详细使用教程见 [我的博客](https://blog.6yfz.cn/tutorial/bot-dingtalk.html)  
1. Fork此项目
2. 在Fork的仓库中添加三个secret(secret,token,mids)
3. 启动GitHub action（fork的仓库默认没开启action）  
4. 点击star开始执行Action（第一次star之后就会自动定时运行）
## 其他
本项目的Action任务参考借鉴于[WakeLeanCloud](https://github.com/blogimg/WakeLeanCloud)  
**本项目目前只实现了基于小刀网的线报推送与bilibili的up主投稿推送，监测间隔是两小时**。  
如果有其他想要实现的功能可以提个issue。  
如果想要更改检测频率请自行修改yml里的corn表达式，详细见[修改时间间隔](#修改时间间隔)。  
执行日志目前仅在action任务中有显示，如果有需要的话可以像WakeLeanCloud一样在仓库添加log文件(提个issue吧)。 
## 修改时间间隔
首先修改 /.github/workflows/DingTalk_misson.yml 文件中的cron表达式，具体语法说明可以参考[官方文档](https://docs.github.com/en/actions/reference/events-that-trigger-workflows#scheduled-events)，如果需要测试可以使用官方提供的测试网站[crontab guru](https://crontab.guru/)  
然后修改 run.py 文件，将 if ac_time<7200 : 中的7200修改为其他时间间隔数值，请注意单位为秒。  
未来或许会优化代码将它统一到yml中修改。

## 未来
- 为了功能多样化与个性化，增加推送订阅的线报、视频以及其他网站，并通过模块化的方案供用户自己选择启用。
- debug info的规范化，使用户能更明了的查看程序的具体运行情况。
- 自动拉取仓库更新
- 添加GitHub action缓存，优化启动速度。
  
以上内容多启发于@JunzhouLiu的仓库[JunzhouLiu/BILIBILI-HELPER](https://github.com/JunzhouLiu/BILIBILI-HELPER#%E4%BD%BF%E7%94%A8-github-actions-%E8%87%AA%E5%8A%A8%E5%90%8C%E6%AD%A5%E6%BA%90%E4%BB%93%E5%BA%93%E4%BB%A3%E7%A0%81)。总之从他人的仓库里学到了很多，意识到了自己还欠缺了很多。也希望自己的代码规范以及内容能向这些大佬看齐。然而独木不成林，非常希望您能看到这段话有感而发，与我共同建设这个项目。