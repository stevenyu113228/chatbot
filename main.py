import os
import sys
import json
import pprint
import telepot
import requests
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction

app = Flask(__name__)

channel_secret = os.environ.get('channel_secret', None)
channel_access_token = os.environ.get('channel_access_token', None)
line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

bot = telepot.Bot(os.environ.get('telegram_token', None))
#//////////////////#
@app.route("/", methods=['GET'])
def index():
    return os.environ.get('index_show', '|ω・`)')

@app.route('/telegram', methods=['POST'])
def telegram():
    body = request.get_data(as_text=True)
    msg = json.loads(body)['message']
    content_type, chat_type, chat_id = telepot.glance(msg)
    chat_id = msg['chat']['id']
    message_id = msg['message_id']
    user_id = msg['from']['id']
    hide_keyboard = {'hide_keyboard': True}

    if content_type == 'text':
        command = msg['text'].lower()
        say = msg['text']
        if command == '/start':
            bot.sendMessage(chat_id,'今天有什麼事要靠北嗎？',reply_markup=hide_keyboard)
    return 'OK'

@app.route("/line", methods=['POST'])
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
    msg = json.loads(body)['events'][0]
    try:
        content_type = msg['message']['type']
        reply_to = msg['replyToken']
        say = msg['message']['text']
        command = say.lower()
    except:
        content_type = msg['type']

    if content_type == 'text':
		line_bot_api.reply_message(reply_to,ltext('尼好'+reply_to+'你剛剛說的是\n'+command))
		line_bot_api.reply_message(reply_to,ltext(str(body)))
        #if command == 'hello':
        #    line_bot_api.reply_message(reply_to,ltext('尼好')
        #else:
        #    line_bot_api.reply_message(reply_to,ltext('h\ni'))
    return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 5000)))
