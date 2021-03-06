# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import tushare as ts
from  datetime  import  *

headers = {
    'Cookie': '_gscu_1042262807=972428447ozpcs69; ccpassport=d277e785b88a56eb0e72f0da2a55f88a; wzwsconfirm=f44934d3368ed61012361b0fd08d400d; wzwsvtime=1511244744; wzwstemplate=OA==; wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDgxNTI0NjU=',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://www.pbc.gov.cn/eportal/fileDir/defaultCurSite/resource/cms/2015/07/2013s07.htm'
r = requests.get(url, headers=headers)
r.encoding = 'utf'
soup = BeautifulSoup(r.text,"lxml")
td_title = soup.find_all("td", class_="xl29")
year_list = map(lambda x: str(x.string).strip().replace(".","-")+"-01", td_title)
year_list.append("2014-12-01")
year_list = [datetime.strptime(x,'%Y-%m-%d') for x in year_list]

tr = soup.find_all("tr",attrs={"style":"mso-height-source:userset;height:19.5pt","height":"26"})

m2_list = map(lambda x: str(x.string).strip(), soup.find_all("td", class_="xl52"))
m2_list = m2_list + map(lambda x: str(x.string).strip(), soup.find_all("td", class_="xl54"))
m2_list = m2_list + map(lambda x: str(x.string).strip(), soup.find_all("td", class_="xl56"))

m1_list = map(lambda x: str(x.string).strip(), tr[2].find_all("td", class_="xl60"))
m1_list = m1_list + map(lambda x: str(x.string).strip(), tr[2].find_all("td", class_="xl61"))
m1_list = m1_list + map(lambda x: str(x.string).strip(), tr[2].find_all("td", class_="xl62"))

m0_list = map(lambda x: str(x.string).strip(), tr[4].find_all("td", class_="xl63"))
m0_list = m0_list + map(lambda x: str(x.string).strip(), tr[4].find_all("td", class_="xl61"))
m0_list = m0_list + map(lambda x: str(x.string).strip(), tr[4].find_all("td", class_="xl62"))

print year_list.__len__()
print m2_list.__len__()
print m1_list.__len__()
print m0_list.__len__()

df = pd.DataFrame(index=year_list,columns=["M2","M1","M0"])
df['M2'] = m2_list
df['M1'] = m1_list
df['M0'] = m0_list
print df
df.to_csv("2013_RMB_SUPPLY.csv",index_label="date")




