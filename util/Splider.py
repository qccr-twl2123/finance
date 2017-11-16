# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': '_gscu_1042262807=972428447ozpcs69; ccpassport=d277e785b88a56eb0e72f0da2a55f88a; wzwsconfirm=66a5c565b5e63b8276f26d51130cee96; wzwsvtime=1510725850; wzwstemplate=MQ==; wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDExMTY1MjM=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125440/125838/125888/2968982/index.html'
r = requests.get(url, headers=headers)
r.encoding = 'utf'
soup = BeautifulSoup(r.text,"lxml")
body = soup.find_all("tbody")[0]
print body
item_list = body.find_all("tr",attrs={"style","height:15pt"})
print item_list

