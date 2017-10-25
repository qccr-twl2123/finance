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
    print index_date.head(10)
    # index_date = index_date[["date","high","close","open"]]

    #======计算海龟交易的买卖点
    N1 =20
    N2 =10
    #计算最近N1个交易日该股票最高价
    index_date['最近N1个交易日股价最高点']= pd.rolling_max(index_date['high'],N1)
    index_date['最近N1个交易日股价最高点'].fillna(value=pd.expanding_max(index_date['high']),inplace=True)
    print index_date['最近N1个交易日股价最高点']

    #计算最近N2个交易日该股票最低价
    index_date['最近N2个交易日股价最低价']=pd.rolling_min(index_date['low'],N2)
    index_date['最近N2个交易日股价最低价'].fillna(value=pd.expanding_min(index_date['low']),inplace=True)
    # print index_date['最近N2个交易日股价最低价']

    #当天的close> 最近N1天交易日的最高价,将收盘发出信号设置为1
    buy_index = index_date[index_date['close'] > index_date['最近N1个交易日股价最高点'].shift(1)].index
    index_date.loc[buy_index,'收盘发出的信号'] = 1
    # 当天的close<最近N2天交易日的最最低价,将收盘发出信号设置为0
    sell_index =  index_date[index_date['close']<index_date['最近N2个交易日股价最低价'].shift(0)].index
    index_date.loc[sell_index,'收盘发出的信号'] =0

    #计算当天的仓位,当天持有上证指数为1,不持有为0
    index_date['当天仓位'] = index_date['收盘发出的信号'].shift(1)
    index_date['当天仓位'].fillna(method='ffill',inplace=True)



    index_date['资金指数'] = (index_date['change'] * index_date['当天仓位'] + 1.0).cumprod()
    inital_idx = index_date.iloc[0]['colse'] /(1+index_date.iloc[0]['change'])
    index_date['资金指数']*=inital_idx

    #计算海龟交易法每日涨跌幅及收益
    index_date["海龟交易法每日涨跌幅"]=index_date['p_change']*index_date['当天仓位']
    print index_date

if __name__=="__main__":
    tutle_trade("600030")

