########## 字典Function 
## Argument:傳入單一中文字
## Return: String 注音符號
## 使用moedict API

import requests
import json

def chinese_bopomofo(word):
    ret_data ='這ㄍ字應該是念做...\n'
    try:
        res = requests.get('https://www.moedict.tw/uni/'+str(word))
        jd = json.loads(res.text)
        for i in jd['heteronyms']:
            if ret_data != '':
                ret_data+='\n'
            ret_data += i['bopomofo']

    except:
        ret_data = '對不起...\n機器人壞掉了\n暫時無法查詢QQ'
    #print(ret_data)
    return ret_data