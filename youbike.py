########## Ubike
## Argument:暫無 (之後新增各站dict)
## Return: String 空位及車數
## 使用Data.Taipei API

import requests
import json

def getubike():
    ret_data = ''
    try:
        url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz'
        res = requests.get(url)
        jd = json.loads(res.text)

        gg = jd['retVal']['0045'] # 公館
        ntust = jd['retVal']['0061'] # 台科

        ret_data = '台科空位 : ' + ntust['bemp'] +'\n' +\
                '台科車數 : ' + ntust['sbi'] + '\n' +\
                '公館空位 : ' + gg['bemp'] + '\n' +\
                '公館車數 : ' + gg['sbi'] + '\n'
    except:
        ret_data = '對不起...\n機器人壞掉了\n暫時無法查詢QQ'
    return ret_data