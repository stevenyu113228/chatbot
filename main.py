import pm25
import weather
import bopomofo
import restaurant
import youbike

########## import函式庫 Start
import os
import sys
import json
import pprint
import requests
import base64
import time
import random

from flask import Flask, request, abort
from flask import render_template, jsonify
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction
##########import函式庫 End

########## Flask與Line Bot Api初始化 Start
## channel_secret -> Line
## channel_access_token -> Line
app = Flask(__name__)
channel_secret = '997f92b4f41d75979553370d0bc24153'
channel_access_token = 'mCB7Cj0StRP5bweTZyLX2SlrdBkZ6gDGE5WgsjgQoC/Me4U3kwBdDx7Cq3OQ1LmGsvenvk+3HlhUXDSi4c3Z8pRoE6BnWM3XKQ425idTQzDqE06E0y+OYEJAcJH0s/VsS5S/tU7VYiD/CsEheE+zTAdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
########## Flask與Line Bot Api初始化 End


######### 以下主程式 Start
@app.route("/", methods=['POST'])
def callback():
    def ltext(reply):
        return TextSendMessage(text=reply)
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    eve = json.loads(body)['events'][0]

    try:
        content_type = eve['message']['type']
        reply_to = eve['replyToken']
        say = eve['message']['text']
        command = say.lower()
    except:
        content_type = eve['message']['type']
        reply_to = eve['replyToken']
        msg_id = eve['message']['id']
    if content_type == 'text':#普通文字
        if command == 'ㄩㄇ':
            line_bot_api.reply_message(reply_to,ltext('不ㄩ'))
        elif command =='安安':
            line_bot_api.reply_message(reply_to,ltext('安安尼好'))
        elif command =='ㄋ4邊緣人ㄇ?':
            line_bot_api.reply_message(reply_to,ltext('你才4邊緣人\n你全家都邊緣人\n森77'))
        elif command =='你好':
            line_bot_api.reply_message(reply_to,ltext('哈囉ㄋ好'))
        elif command =='help':
            rp = '嗨嗨!!!\n'+\
            '歡迎使用廢文機器人\n'+\
            '使用廢文機器人之前\n'+\
            '敬請注意以下幾件事情\n'+\
            '1.請勿拍打餵食\n'+\
            '2.別對我講怪怪的話(?\n'+\
            '3.本機器人可能會不定期維護\n'+\
            '3.查詢指令請輸入「command」\n'+\
            '4.查看作者請輸入「about」\n'+\
            '感謝您的配合:)'
            line_bot_api.reply_message(reply_to,ltext(rp))
            #print (rp)
        elif command =='command':
            rp ='1.輸入「注音：字」可查詢該字的注音\n'+\
                '2.發給我照片(僅限個人照)可自動辨識照片中人物的年齡與性別\n'+\
                '3.傳送定位給我可以查詢當地天氣\n'+\
                '4.輸入「吃」相關句子可自動幫你選擇今天要吃什麼喔！(僅限台科大餐廳使用)\n'+\
                '除此之外\n'+\
                '還有非常多隱藏版的功能等待大家來發掘\n'+\
                '謝謝大家！！'
            line_bot_api.reply_message(reply_to,ltext(rp))
            #print (rp)        
        elif command =='about':
            rp ='安安!!\n'+'我叫做游照臨\n'+\
                '目前就讀台科大電機系二年級\n'+\
                '至於為什麼我要做這個APP呢?\n'+\
                '因為我暑假太無聊了...ㄏㄏ\n'+\
                '如果對於這個APP有任何建議\n'+\
                '請各位email給我\n'+\
                'b10507004@mail.ntust.edu.tw\n'+\
                '感謝各位的支持!!\n'
            line_bot_api.reply_message(reply_to,ltext(rp))
            #print (rp) 
        elif '注音' in command:
            command = command[command.find("：")+1:]
            line_bot_api.reply_message(reply_to,ltext(bopomofo.chinese_bopomofo(command)))
        elif any(x in command for x in ['吃','餐']):
            line_bot_api.reply_message(reply_to,ltext(restaurant.ntust_restaurant(command)))
        else:
            #line_bot_api.reply_message(reply_to,ltext(str(body)))
            rp = '對ㄅ起...我笨笨\n'+\
                 '聽ㄅ懂你在說什麼\n'+\
                 '請使用「help」來看我這ㄍ廢廢機器人能幹嘛'
            line_bot_api.reply_message(reply_to,ltext(rp))
    elif content_type == 'location': #定位
        lat = eve['message']['latitude']
        lon = eve['message']['longitude']
        line_bot_api.reply_message(reply_to, ltext(weather.get_weather(lat,lon)))
    return 'OK'
########## 主程式 Stop


########## Main Function Start
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9487,debug=True,threaded=True)
########## Main Function Stop

