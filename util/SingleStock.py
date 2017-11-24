#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class  SingleStock(object):

    def __init__(self, code):
        self.__code = code

    def get_stock_hist(self):
        return ts.get_hist_data(self.__code)

    def get_stock_basic(self,tag):
        return ts.get_stock_basics().ix[self.__code][tag]

    def show_close_curve_shape(self):
        df = self.get_stock_hist()
        x = pd.to_datetime(df.index,format="%Y-%m-%d")
        close_price_list = df["close"].T.values
        open_price_list = df['open'].T.values
        stock_name = self.get_stock_basic("name")

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.plot(x, close_price_list, c='red',label="收盘价")
        plt.plot(x, open_price_list, c='y',label="开盘价")
        plt.xlabel("交易日期")
        plt.ylabel("收盘价")
        plt.title(stock_name,loc="right")
        plt.xticks(rotation="45")
        plt.show()

if __name__ == '__main__':
    stock_code = "600030"
    singleStock = SingleStock(stock_code)
    singleStock.show_close_curve_shape()