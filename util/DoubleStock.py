#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import ffn
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class StockKit(object):

    def __init__(self, stock_list):
        self.__stock_list = stock_list

    def get_stock_hsit(self):
        stock_hist_dict = {}
        for stock_code in self.__stock_list:
            stock_hist_dict[stock_code] = ts.get_hist_data(stock_code)
        return stock_hist_dict

    def get_stock_hist_by_code(self,code):
        return self.get_stock_hsit()[code]

    def get_stock_name_by_code(self,code):
        return ts.get_stock_basics().ix[code]['name']

    def scatter(self, start_date):
        stock_x = self.get_stock_hist_by_code(self.__stock_list[0])
        stock_y = self.get_stock_hist_by_code(self.__stock_list[1])
        stock_x = stock_x[stock_x.index > start_date].sort_index(ascending=True)
        stock_y = stock_y[stock_y.index > start_date].sort_index(ascending=True)

        stock_x_name = self.get_stock_name_by_code(self.__stock_list[0])
        stock_y_name = self.get_stock_name_by_code(self.__stock_list[1])

        stock_x_return_index = ffn.to_returns(stock_x['close'])
        stock_y_return_index = ffn.to_returns(stock_y['close'])
        title = stock_x_name + "-" + stock_y_name + "收益率"
        plt.scatter(stock_x_return_index, stock_y_return_index, color="r")
        plt.title(title)
        plt.xlabel(stock_x_name)
        plt.ylabel(stock_y_name)
        print stock_x_return_index.corr(stock_y_return_index)
        plt.show()

    def compare_for_basic(self, start_date):
        stock_x = self.get_stock_hist_by_code(self.__stock_list[0])
        stock_y = self.get_stock_hist_by_code(self.__stock_list[1])
        stock_x = stock_x[stock_x.index > start_date].sort_index(ascending=True)
        stock_y = stock_y[stock_y.index > start_date].sort_index(ascending=True)

        stock_x_name = self.get_stock_name_by_code(self.__stock_list[0])
        stock_y_name = self.get_stock_name_by_code(self.__stock_list[1])
        print stock_x_name
        print stock_x.describe()

        print stock_y_name
        print stock_y.describe()



if __name__ == '__main__':
    stock_code_list = ["002624","601336"]
    stockKit = StockKit(stock_code_list)
    stockKit.scatter("2017-01-01")
    stockKit.compare_for_basic("2017-01-01")
