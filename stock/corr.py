#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import  pandas as pd
from scipy import stats
import  numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

hsh = ts.get_hist_data("002594").truncate(after='2017-10-01')
hsh['收益率']= hsh['price_change']/hsh['close']
x = hsh['收益率']

mt = ts.get_hist_data("600519").truncate(after='2017-10-01')
mt['收益率'] = mt.truncate(after='2017-10-01')["price_change"]/mt['close']
y = mt['收益率']

plt.scatter(x,y)
plt.title("煌上煌与茅台收益率散点图")
plt.xlabel("煌上煌收益率")
plt.ylabel("茅台收益率")
plt.show()
print "相关系数:" + x.corr(y)

