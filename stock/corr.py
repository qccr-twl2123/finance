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

class StockCorr(object):

    def __init__(self,stock_list,truncate):
        self.stock_list = stock_list
        self.truncate = truncate

    def scatter(self):
        stock_add_return_index = []
        stock_name_list = []
        for stock_name in self.stock_list:
            stock_hist = ts.get_hist_data(stock_name).truncate(after=self.truncate)
            stock_hist['return_index'] = stock_hist['price_change']/stock_hist['close']
            stock_add_return_index.append(stock_hist)
            stock_name_list.append(ts.get_stock_basics().ix[stock_name]['name'])

        x = stock_add_return_index[0]['return_index']
        y = stock_add_return_index[1]['return_index']
        title = stock_name_list[0]+"与"+stock_name_list[1] +"收益率散点图"
        plt.scatter(x,y,color="r")
        plt.title(title)
        plt.xlabel(stock_name_list[0]+"return_index")
        plt.ylabel(stock_name_list[1]+"return_index")
        print stock_add_return_index[0].return_index.corr(stock_add_return_index[1].return_index)
        plt.show()


if __name__ == '__main__':
       stock_code_list =["601398","601857"]
       stock_corr =  StockCorr(stock_code_list,"2017-10-01")
       stock_corr.scatter()