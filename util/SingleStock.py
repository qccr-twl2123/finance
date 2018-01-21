#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
import ffn
import numpy as np
from scipy.stats import norm
reload(sys)
sys.setdefaultencoding('utf-8')

class  SingleStock(object):

    def __init__(self, code):
        self.__code = code

    def get_stock_hist(self):
        return ts.get_hist_data(self.__code)

    def get_stock_basic(self, tag):
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

    def get_return_index(self, start_date):
        df = self.get_stock_hist()
        df = df[df.index >= start_date].sort_index(ascending = True)
        close_price = df['close']
        return_index = ffn.to_returns(close_price)

        x = [pd.to_datetime(i,format="%Y-%m-%d") for i in return_index.index]
        y = [y for y in return_index.T.values]

        plt.plot(x, y, c="red", label="收益率")
        plt.xlabel("日期")
        plt.ylabel("收益率")
        plt.title(self.get_stock_basic("name")+"历史收益率", loc="right")
        plt.xticks(rotation="45")
        plt.show()

    def value_at_risk(self, start_date):
        df = self.get_stock_hist()
        df = df[df.index >= start_date].sort_index(ascending=True)
        close_price = df['close']
        return_index = ffn.to_returns(close_price)

        # 历史模拟法

        # 协方差估计法
        print norm.ppf(0.05, return_index.mean(), return_index.std())

    def basic_figure(self, start_date):
        df = self.get_stock_hist()
        df = df[df.index >= start_date].sort_index(ascending = True)
        close_price = df['close']
        return_index = ffn.to_returns(close_price)
        x = [pd.to_datetime(i,format="%Y-%m-%d") for i in return_index.index]
        stock_name = self.get_stock_basic("name")

        plt.figure(figsize=(16, 6))
        plt.subplot(121)
        y = [y for y in return_index.T.values]

        plt.plot(x, y, c="red", label="收益率")
        plt.xlabel("日期")
        plt.ylabel("收益率")
        plt.title(stock_name+"历史收益率", loc="right")
        plt.xticks(rotation="45")

        plt.subplot(122)
        return_index.cumprod()
        plt.plot(return_index.cumprod())
        plt.show()




if __name__ == '__main__':

    stock_code = "600688"
    singleStock = SingleStock(stock_code)
    # singleStock.show_close_curve_shape()
    # singleStock.get_return_index("2016-11-01")
    # singleStock.value_at_risk("2017-11-01")
    singleStock.basic_figure("2017-11-01")