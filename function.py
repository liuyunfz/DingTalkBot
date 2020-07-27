# -*- coding: utf-8 -*-
import time,requests,json
from lxml import etree
#获取小刀网线报
def get_message():
    url="https://www.x6d.com/html/34.html"
    rsp=requests.get(url=url)
    s=etree.HTML(rsp.text)
    print("log:网页状态码：",rsp.status_code)
    s=s.xpath("//li[@class='layui-clear']")
    print(len(s))
    urls=[]
    imgs=[]
    infos=[]
    for item in s:
        x=item.xpath("./div/div[1]/a/@href")
        img=item.xpath("./div/div[1]/a/img/@src")
        info_xpath=item.xpath("./div/div[2]/div[1]/text()")
        urls.append("https://www.x6d.com{}".format(x[0]))
        imgs.append("https://www.x6d.com{}".format(img[0]))
        infos.append(info_xpath[0].strip())
    return zip(urls,imgs,infos)
    