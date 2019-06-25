# coding=utf-8
import time
from aip import AipSpeech
import requests
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

import city_dict
import itchat
import linecache
import random



# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):


    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:


        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        if msg['Text'][0:2]=="功能":
            return "----------====功能===----------\n 1、给你查天气 例如输入\n        查天气合肥\n 2、给你讲笑话 例如输入\n        我要听笑话嘻嘻 或 2\n 3、我想对你说 输入\n        快告诉我 或 3\n 4、文字转语音 例如输入 \n  （1）40我开心：将我开心以女声转为语音 \n  （2）41我开心：将我开心以男声转为语音 \n  （3）43我开心：将我开心以情感合成1转为语音 \n   （4）44我开心：将我开心以情感合成2转为语音\n 5、我要小可爱 例如输入\n        (1)51(静态图)\n        (2)52(动态图 )\n 6、待开发emmm"

        if msg['Text'][1:3] == "天气":
            city = msg['Text'][3:5]
            return weather(city,msg)

        if msg['Text'][3:5] == "笑话" or msg['Text'] == "2":
            return joke()

        if msg['Text'][0:2] == "快告" or msg['Text'] == "3":
            return lovewords()

        if msg['Text'][0:1] == "4" :
            if  msg['Text'][1:2] == "0" or msg['Text'][1:2] == "1" or msg['Text'][1:2] == "3" or msg['Text'][1:2] == "4":
                file='@fil@'+ transliteration(msg['Text'][1:2],msg['Text'][2:])
                return file

        if msg['Text'][0:1] == "5" :
            friend = itchat.search_friends(msg['User']['NickName'])[0]
            if msg['Text'][1:] == "1" :
                itchat.send_image(doutu(), friend["UserName"])
            if msg['Text'][1:] == "2" :
                itchat.send_file(dongtu(), friend["UserName"])




    # 当消息是由自己发出的时候 测试++++++++++++++++
    if  msg['FromUserName'] == myUserName:




        #功能模块
        if msg['Text'][0:2]=="功能":
            print("----------====功能===----------\n 1、给你查天气 例如输入\n        查天气合肥\n 2、给你讲笑话 例如输入\n        我要听笑话嘻嘻 或 2\n 3、我想对你说 输入\n        快告诉我 或 3\n 4、文字转语音 例如输入 \n  （1）40我开心：将我开心以女声转为语音 \n  （2）41我开心：将我开心以男声转为语音 \n  （3）43我开心：将我开心以情感合成1转为语音 \n   （4）44我开心：将我开心以情感合成2转为语音\n 5、我要小可爱 例如输入\n        (1)51(静态图)\n        (2)52(动态图 )\n 6、待开发emmm"
                )
            itchat.send("----------====功能电脑===----------\n 1、给你查天气 例如输入\n        查天气合肥\n 2、给你讲笑话 例如输入\n        我要听笑话嘻嘻 或 2\n 3、我想对你说 输入\n        快告诉我 或 3\n 4、文字转语音 例如输入 \n  （1）40我开心：将我开心以女声转为语音 \n  （2）41我开心：将我开心以男声转为语音 \n  （3）43我开心：将我开心以情感合成1转为语音 \n   （4）44我开心：将我开心以情感合成2转为语音\n 5、我要小可爱 例如输入\n        (1)51(静态图)\n        (2)52(动态图 )\n 6、待开发emmm", 'filehelper')
        if msg['Text'][1:3]=="天气":
            city=msg['Text'][3:5]
            weather(city,msg)
            itchat.send(weather(city,msg),'filehelper')
        if msg['Text'][3:5] == "笑话" or msg['Text'] == "2":
            itchat.send(joke(),'filehelper')
        if msg['Text'][0:2] == "快告" or msg['Text'] == "3":
            itchat.send(lovewords(),'filehelper')
        if msg['Text'][0:1] == "4" :
            if  msg['Text'][1:2] == "0" or msg['Text'][1:2] == "1" or msg['Text'][1:2] == "3" or msg['Text'][1:2] == "4":
                file='@fil@'+ transliteration(msg['Text'][1:2],msg['Text'][2:])
                itchat.send(msg=file, toUserName='filehelper')
        if msg['Text'][0:1] == "5":
            if msg['Text'][1:] == "1":
                itchat.send_image(doutu(), 'filehelper')
            if msg['Text'][1:] == "2":
                itchat.send_file(dongtu(),  'filehelper')


def  dongtu():
    count = random.randrange(1, 3)
    file = 'gif/gif%d' % (count) + '.gif'
    return file
#斗图 静态图
def doutu():
    count=random.randrange(1, 3)

    file='jpg/img%d'%(count)+'.jpg'
    return file
    print(file)

#文字转语音
def transliteration(perc,msgtext):
    """ 你的 APPID AK SK """
    APP_ID = '16532499'
    API_KEY = 'XMMxzi1sCsGGaYFstjok7WQq'
    SECRET_KEY = 'sPP47Nz7k18UGZfbDgNXfjkTjrG05agq'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(msgtext, 'zh', 1, {
        'vol': 5, 'per': perc
    })
    # per 发音人选择 0：女声 1：男生 3：情感合成-度逍遥 4 情感合成-度丫丫
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
        return 'auido.mp3'

#土味情话
def lovewords():
    # 文件总行数
    f = open('sao.txt', 'r', encoding='UTF-8')
    cont = f.readlines()
    for i in range(1):
        a = random.randrange(1, len(cont))  # 1-9中生成随机数

        # 从文件sao.txt中对读取第a行的数据
        theline = linecache.getline('sao.txt', a)
        print(theline)
    return theline

#讲笑话
def joke():
    """
      随机获取笑话段子列表(https://github.com/MZCretin/RollToolsApi#%E9%9A%8F%E6%9C%BA%E8%8E%B7%E5%8F%96%E7%AC%91%E8%AF%9D%E6%AE%B5%E5%AD%90%E5%88%97%E8%A1%A8)
      :return: str,笑话。
    """
    print('获取随机笑话...')
    try:
        resp = requests.get('https://www.mxnzp.com/api/jokes/list/random')
        # print(resp.text)
        if resp.status_code == 200:
            content_dict = resp.json()
            if content_dict['code'] == 1:
                # 每次返回 10 条笑话信息，只取一次
                return_text = content_dict['data'][0]['content']
                # print(return_text)
                print(return_text)
                return return_text
            else:
                print(content_dict['msg'])
        print('获取笑话失败。')
    except Exception as exception:
        print(exception)


#查天气
def weather(city,msg):
    print(city_dict.city.get(city))#城市对应编码
    """
        获取天气信息。网址：https://www.sojson.com/blog/305.html .
       :param city_name: str,城市名
       :return: str ,例如：2019-06-12 星期三 晴 南风 3-4级 高温 22.0℃ 低温 18.0℃ 愿你拥有比阳光明媚的心情
       """
    cityy="查询天气地点"+city
    weather_url = f'http://t.weather.sojson.com/api/weather/city/{city_dict.city.get(city)}'
    resp = requests.get(url=weather_url)
    weather_dict = resp.json()
    # 今日天气
    # {
    # "sunrise": "04:45",
    # "high": "高温 34.0℃",
    # "low": "低温 25.0℃",
    # "sunset": "19:37",
    # "aqi": 145,
    # "ymd": "2019-06-12",
    # "week": "星期三",
    # "fx": "西南风",
    # "fl": "3-4级",
    # "type": "多云",
    # "notice": "阴晴之间，谨防紫外线侵扰"
    # }
    today_weather = weather_dict.get('data').get('forecast')[0]

    display = ['ymd', 'week', 'type', 'fx', 'fl', 'high', 'low', 'notice']
    weather_info = '\n'.join(today_weather[p] for p in display if today_weather.get(p, None))

    start_datetime = datetime.datetime(2016, 8, 19)

    dictum_msg = ''
    sweet_words = '来自 Starry the Night'
    # 在一起，一共多少天了
    now_datetime = datetime.datetime.now()
    day_delta = (now_datetime - start_datetime).days
    delta_msg = f'这是我们认识的第 {day_delta} 天'



    weather_msg = f'\n{delta_msg}。\n{cityy}\n{weather_info }\n{dictum_msg}\n{sweet_words}\n'
    print(weather_msg)
    return weather_msg



def get_response(msg):
    #茉莉机器人官网（http://www.itpk.cn/）申请账号->个人中心->获得Api key and Api Secret：
    moli_api_url = 'http://i.itpk.cn/api.php'
    moli_data={
        "question": msg,
        "api_key":"ac00db995a4a8f2a3f3623c82f3cc9d9",
        "api_secret":"anaoutswrz1y"
    }
    # 我们通过如下命令发送一个post请求
    r = requests.post(moli_api_url, data = moli_data)
    return r.text
#用于接收来自朋友间的对话消息  #如果不用这个，朋友发的消息便不会自动回复
#@itchat.msg_register(itchat.content.TEXT)
#def print_content(msg):
   # return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
#用于接收群里面的对话消息
def print_content(msg):
    if msg['Text'][0:5]=='@MISS':

        print(msg['Text'])
        return get_response(msg['Text'][5:])


if __name__ == '__main__':

    #itchat.auto_login()
    # 实现登录和登录状态保存
    #itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.auto_login(hotReload=True)
    itchat.dump_login_status()

    myUserName = itchat.get_friends(update=True)[0]["UserName"]

    itchat.run()

