import requests
import json
def get_pm25():
    url = 'https://pm25.lass-net.org/data/last-all-epa.json'
    ret_data = ''
    try:
        res = requests.get(url)
        jd = json.loads(res.text)
        for i in jd['feeds'] :
            if i['SiteName'] == '古亭' :
                ret_data = '監測站 : ' + str(i['SiteName'])+'\n'+\
                'PM2.5 : ' + str(i['PM2_5_AVG'])+'\n' +\
                'PM10 : ' + str(i['PM10_AVG']) +'\n'+\
                i['Status']
    except:
        ret_data = 'Server EOFError'
    return ret_data