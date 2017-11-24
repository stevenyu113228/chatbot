########## 學生餐廳Function S
## Argument:使用者傳入字串
## Return:String 餐廳名稱
import random
def ntust_restaurant(command):
    command = str(command)
    restaurant = [
        ['摩斯','美而美','嚴茶','溫州大餛飩','四海遊龍','上品排骨','台式早餐','一日三餐','自助餐','地中海','鐵板','丼太郎','甘味食堂','7-11'],
        ['7-11','麵包店','美而美','豪享來','滷味','雞同鴨講','八方雲集','自助餐','日和','藝素佳','蔥抓餅','阿水'],
        ['自助餐','快餐'],
        ['炒飯','炒麵','鹹水雞','鹹酥雞']
    ]
    out = '等一下ㄘ '
    store = [
        ['1','一'],
        ['3','三'],
        ['教'],
        ['後']
    ]
    if any(x in command for x in store[0]):
        out += restaurant[0][random.randrange(0,len(restaurant[0]))]
    elif any(x in command for x in store[1]):
        out += restaurant[1][random.randrange(0,len(restaurant[1]))]
    elif any(x in command for x in store[2]):
        out += restaurant[2][random.randrange(0,len(restaurant[2]))]
    elif any(x in command for x in store[3]):
        out += restaurant[3][random.randrange(0,len(restaurant[3]))]
    else:
        num = int(random.randrange(0,len(restaurant)))
        if num == 0:
            out += '一餐的'
        elif num == 1:
            out += '三餐的'
        elif num == 2:
            out += '教餐的'
        elif num == 3:
            out += '後餐的'
        out += restaurant[num][random.randrange(0,len(restaurant[num]))]
    #print (out)
    return out