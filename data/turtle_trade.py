#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_hist_data(code):
    return ts.get_hist_data(code)

def tutle_trade(code):
    index_date = pd.read_csv("000875.csv")
    # index_date = index_date[["date","high","close","open"]]

    #======计算海龟交易的买卖点
    N1 =20
    N2 =10
    #计算最近N1个交易日该股票最高价
    index_date['最近N1个交易日股价最高点']= pd.rolling_max(index_date['high'],N1)

    index_date['最近N1个交易日股价最高点'].fillna(value=pd.expanding_min(index_date['low']),inplace=True)
    print index_date['最近N1个交易日股价最高点']


if __name__=="__main__":
    tutle_trade("600030")

