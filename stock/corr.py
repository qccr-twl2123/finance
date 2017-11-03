#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import  pandas as pd
from scipy import stats
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

hsh = ts.get_hist_data("002594")
hsh['收益率']= hsh.truncate(after='2017-10-01')['price_change']/hsh['close']

mt = ts.get_hist_data("600519")
mt['收益率'] = mt.truncate(after='2017-10-01')["price_change"]/mt['close']

plt.scatter(hsh['收益率'],mt['收益率'])
plt.title("煌上煌与茅台收益率散点图")
plt.xlabel("煌上煌收益率")
plt.ylabel("茅台收益率")
plt.show()
print "相关系数:" + hsh['收益率'].corr(mt['收益率'])

