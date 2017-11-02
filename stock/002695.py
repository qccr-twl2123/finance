#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import  pandas as pd
from scipy import stats
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 煌上煌股票分析

hsh = ts.get_hist_data("000768")
# print hsh

hsh['收益率']= hsh['price_change']/hsh['close']
# print  hsh.loc[:,['close','price_change','收益率']]

print hsh.truncate(after='2017-05-01')['收益率'].describe()
print stats.norm.ppf(0.05,hsh.truncate(after='2017-09-01')['收益率'].mean(),hsh.truncate(after='2017-05-01')['收益率'].var() * 0.5)

# plt.plot(hsh.truncate(after='2017')['收益率'])
# plt.show()