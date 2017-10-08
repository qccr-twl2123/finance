#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts

def get_hist_data(code):
    return ts.get_hist_data(code)

def get_hist_data_plot():
    return None

if __name__=="__main__":
    print  get_hist_data("600871")
