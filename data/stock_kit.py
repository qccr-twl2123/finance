#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt

def get_hist_data(code):
    return ts.get_hist_data(code)


def show_stock_figure(df):
    x = df.index
    y = df["close"].T.values
    plt.plot(x,y)
    plt.show()


if __name__=="__main__":
    print get_hist_data("002148")
