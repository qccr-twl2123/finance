# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {
    'Cookie': '_gscu_1042262807=972428447ozpcs69; ccpassport=d277e785b88a56eb0e72f0da2a55f88a; wzwsconfirm=f44934d3368ed61012361b0fd08d400d; wzwsvtime=1511244744; wzwstemplate=OA==; wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDgxNTI0NjU=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2014s07.htm'
r = requests.get(url, headers=headers)
r.encoding = 'utf'
soup = BeautifulSoup(r.text,"lxml")
td_title = soup.find_all("td", class_="xl29")
year_list = map(lambda x: str(x.string).strip(), td_title)

tr = soup.find_all("tr",attrs={"style":"mso-height-source:userset;height:19.5pt","height":"26"})

m2_list = map(lambda x: str(x.string).strip(), soup.find_all("td", class_="xl57"))
m2_list = m2_list + map(lambda x: str(x.string).strip(), soup.find_all("td", class_="xl59"))

m1_list = map(lambda x: str(x.string).strip(), tr[2].find_all("td", class_="xl64"))
m1_list = m1_list+ map(lambda x: str(x.string).strip(), tr[2].find_all("td", class_="xl65"))

m0_list = map(lambda x: str(x.string).strip(), tr[4].find_all("td", class_="xl66"))
m0_list = m0_list + map(lambda x: str(x.string).strip(), tr[4].find_all("td", class_="xl64"))
m0_list = m0_list + map(lambda x: str(x.string).strip(), tr[4].find_all("td", class_="xl65"))
print year_list
print m2_list
print m1_list
print m0_list





