# -*- coding: utf-8 -*-
import time
import requests
import json
from lxml import etree
# 获取小刀网线报


def get_message():
    url = "https://www.x6d.com/html/34.html"
    rsp = requests.get(url=url)
    s = etree.HTML(rsp.text)
    print("log:网页状态码：", rsp.status_code)
    s = s.xpath("//li[@class='layui-clear']")
    print(len(s))
    urls = []
    imgs = []
    infos = []
    for item in s:
        x = item.xpath("./div/div[1]/a/@href")
        img = item.xpath("./div/div[1]/a/img/@src")
        info_xpath = item.xpath("./div/div[2]/div[1]/text()")
        urls.append("https://www.x6d.com{}".format(x[0]))
        imgs.append("https://www.x6d.com{}".format(img[0]))
        infos.append(info_xpath[0].strip())
    return zip(urls, imgs, infos)


def get_video(mids: str):
    mid_list = mids.split(',')
    for i in mid_list:
        url = 'https://api.bilibili.com/x/space/arc/search?mid={}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'.format(
            i)
        rsp = requests.get(url)
        datas = rsp.json()['data']['list']['vlist']
        return datas
