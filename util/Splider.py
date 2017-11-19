# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': '_gscu_1042262807=972428447ozpcs69; ccpassport=d277e785b88a56eb0e72f0da2a55f88a; wzwsconfirm=36151d4cdadaabd28ce5f47496c11ccd; wzwsvtime=1510822210; wzwstemplate=NQ==; wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDUxMzU5Njc=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2014s07.htm'
r = requests.get(url, headers=headers)
r.encoding = 'utf'
# print r.text
soup = BeautifulSoup(r.text,"lxml")
item_title = soup.find_all("td",class_="xl30")
print item_title



