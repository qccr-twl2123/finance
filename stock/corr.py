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
        stock_return_index_list = []
        stock_name_list = []
        for stock_name in self.stock_list:
            stock_hist = ts.get_hist_data(stock_name).truncate(after=self.truncate)
            stock_hist['收益率'] = stock_hist['price_change']/stock_hist['close']
            stock_return_index_list.append(stock_hist['收益率'])
            stock_name_list.append(ts.get_stock_basics().ix[stock_name]['name'])

        x = stock_return_index_list[0]
        y = stock_return_index_list[1]
        title = stock_name_list[0]+"与"+stock_name_list[1] +"收益率散点图"
        plt.scatter(x,y,color="r")
        plt.title(title)
        plt.xlabel(stock_name_list[0]+"收益率")
        plt.ylabel(stock_name_list[1]+"收益率")
        print x.T.values
        print x
        # print "相关系数:" + x.corr(y)
        plt.show()


if __name__ == '__main__':
       stock_code_list =["601398","601939"]
       stock_corr =  StockCorr(stock_code_list,"2017-10-01")
       stock_corr.scatter()