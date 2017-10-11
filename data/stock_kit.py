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
    df = ts.get_stock_basics()
    return  df.ix[code]['name'],ts.get_hist_data(code)


def show_stock_figure(name,df):
    x = pd.to_datetime(df.index,format="%Y-%m-%d")
    y = df["close"].T.values

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.plot(x,y,c='red')
    plt.xlabel("交易日期")
    plt.ylabel("收盘价")
    plt.title(name,loc="right")
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__=="__main__":
     name,bwkj = get_hist_data("002148")
     show_stock_figure(name,bwkj[bwkj.index>'2017-08-25'])
