#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class StockKit(object):

    def __init__(self, stock_code_list):
        self.__stock_code_list = stock_code_list

    def get_stock_hsit(self):
        stock_hist_dict = {}
        for stock_code in self.__stock_code_list:
            stock_hist_dict[stock_code] = ts.get_hist_data(stock_code)
        return stock_hist_dict

    def get_stock_hist_by_code(self,code):
        return self.get_stock_hsit()[code]

    def get_stock_basic(self,code):
        return ts.get_stock_basics().ix[code]



if __name__ == '__main__':
    stock_code_list=["002371","600789"]
    stockKit = StockKit(stock_code_list)
    # print  stockKit.get_stock_hsit()
    # print stockKit.get_stock_hist_by_code("002371")
    print stockKit.get_stock_basic("002371")