#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts

def get_stock_data(code):
    return ts.get_hist_data(code)


if __name__=="__main__":
    print  get_stock_data("600871")
