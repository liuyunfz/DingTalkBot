# DingTalkBot
## 这是什么
基于python写的钉钉机器人，通过GitHub Action定时任务实现自动化。
## 有什么用
可以零成本创建属于自己的钉钉机器人，定时推送订阅内容（例如优惠消息等线报亦或是喜欢UP主的更新）。
## 如何使用
1. Fork此项目
2. 在Fork的仓库中添加两个secret
3. 点击star开始执行Action（第一次star之后就会自动定时运行）
## 其他
本项目的Action任务参考借鉴于[WakeLeanCloud](https://github.com/blogimg/WakeLeanCloud)  
**本项目目前只实现了基于小刀网的线报推送，监测间隔是两小时**。如果有其他想要实现的功能可以提个issue。  
如果想要更改检测频率请自行修改yml里的corn表达式。需要注意的是中国的时区是UTC+8，也就是需要额外加上28000秒，这点在代码中也有体现。  
执行日志目前仅在action任务中有显示，如果有需要的话可以像WakeLeanCloud一样在仓库添加log文件。

