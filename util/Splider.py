# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import requests

headers = {
    'Cookie': '_gscu_1042262807=972428447ozpcs69; ccpassport=22bce01f02221818e5251f4365225439; wzwsconfirm=89349685405c82c4de5a57ca4b6bb86c; wzwsvtime=1510459197; wzwstemplate=NA==; wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDQxMzEwODc=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125440/125838/125888/2968982/index.html'
r = requests.get(url, headers=headers)
r.encoding = 'utf'
print r.text