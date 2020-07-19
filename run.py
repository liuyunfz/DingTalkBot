#python 3.8 
import time,hmac,hashlib,base64,urllib.parse,sys,requests,json
from lxml import etree
def sent_message(text:str,title:str,picUrl:str,messageUrl:str):
    try:
        token=sys.argv[1]
        secret = sys.argv[2]
    except:
        print('secret loss')
    timestamp = str(round(time.time() * 1000))  
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    print(timestamp)
    print(sign)
    url="https://oapi.dingtalk.com/robot/send?access_token={2}&timestamp={0}&sign={1}".format(timestamp,sign,token)
    data={
        "msgtype": "link", 
        "link": {
            "text": text, 
            "title": title, 
            "picUrl": picUrl, 
            "messageUrl": messageUrl
        }
    }
    headers={"Content-Type": "application/json"}
    data=json.dumps(data)
    rsp=requests.post(url=url,data=data,headers=headers)
    print(rsp.json().get('errmsg'))
def get_message():
    url="https://www.x6d.com/html/34.html"
    rsp=requests.get(url)
    s=etree.HTML(rsp.text)
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
    nowtime=time.time()
    for url,img,info in zip(urls,imgs,infos):
        rsp=requests.get(url=url)
        break_flag=False
        s=etree.HTML(rsp.text)
        title=s.xpath("//h1[@class='article-title']")[0].text
        date=s.xpath("//time")[0].xpath('string(.)')        
        timeArray = time.strptime(date+":00", "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)
        ac_time=nowtime-timestamp+28800
        #默认时间频率为两小时，单位秒即7200，可以根据自己需求更改。中国为东八区，比标准时间快8小时。
        if ac_time<7200 :
         sent_message(date+"\n"+info,title,img,url)
         print("log:",date,title,info)
        else:
            break_flag=True
        if break_flag==True:
            break 
get_message()