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


def show_sz50s_close_price(stocks):
    codeList = stocks["code"].T.values
    nameList = stocks["name"].T.values

    codeToName = dict(zip(codeList,nameList))

    plt.figure(1,figsize=(20, 8))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    for code  in codeList:
        print  code
        df = get_hist_data(str(code))
        x = pd.to_datetime(df.index,format="%Y-%m-%d")
        y = df["close"].T.values
        plt.figure(1)
        plt.plot(x,y, label=codeToName[code])

    plt.figure(1)
    plt.xlabel("交易日期")
    plt.ylabel("收盘价")
    plt.title("上证50成分股收盘走势",loc="right")
    plt.gcf().autofmt_xdate()
    plt.legend(loc=2)
    plt.show()

if __name__=="__main__":

      print  type(ts.get_sz50s()["code"].T.values)
      # show_sz50s_close_price(ts.get_sz50s())

     # guofang = pd.read_csv("guofang.csv")
     # print guofang
     #
     # show_sz50s_close_price(guofang)
     # name,bwkj = get_hist_data("002695")
     #show_stock_figure(name,bwkj[bwkj.index>'2017-01-25'])
