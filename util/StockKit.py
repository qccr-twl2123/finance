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

    def __init__(self,stock_code):
        self.__stock_code = stock_code

    def get_stock_hsit(self):
        return ts.get_hist_data(self.__stock_code)

