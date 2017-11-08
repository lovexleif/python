#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
  
'''通过聚合数据天气API，获取天气信息'
 2017-10-27
 by:183
'''
 
  
#天气预报查询接口

import requests
import urllib.parse
def showmsg(js):
    #显示时间
    date=js['result']['realtime']
    print('地点:{0} 现在时间：{1} 农历：{2} {3}'.format(date['city_name'],date['date'],date['moon'],date['time']))
    #预报天气状况
    weather=js['result']['weather'] 
    weinfo=weather[0]['info']
    for k,v in weinfo.items():
        print(k,':',v)
    print()
    #显示污染指数
    pm=js['result']['pm25']['pm25']
    print('今天污染指数：\npm25={0} pm10={1} 污染等级{2}:{3}\n生活建议：{4}'.format(pm['pm25'],pm['pm10'],pm['level'],pm['quality'],pm['des']))
    #显示生活建议
    info=js['result']['life']['info']
    f={'ziwaixian':'紫外线','kongtiao':'空调','wuran':'污染','ganmao':'感冒','xiche':'洗车','yundong':'运动', 'chuanyi':'穿衣'}
    for k,v in info.items():
        print(f[k],':',v)

appkey='c57d65a31867911a53e09f769072e000'
city=input('请输入查询的地名：')
value={
    'format':2,
    'key':appkey,
    'cityname':urllib.parse.quote(city),
}
url='http://api.avatardata.cn/Weather/Query'
s=requests.get(url,params=value)
print (type(s))
js=s.json()
showmsg(js)
