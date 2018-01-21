#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import tushare as ts


class Company(object):

    def __init__(self, data_source):
        self.data_source = data_source

    def convert_csv_to_pd(self):
        return pd.read_csv(self.data_source, index_col="date")

    def bar(self):
        fig = plt.figure(1)
        ax1 = plt.subplot(111)
        df = company.convert_csv_to_pd()
        data = (df['stock'].T.values).tolist()
        width = 0.5
        x_bar = np.arange(len(data))
        rect = ax1.bar(left=x_bar,height=np.array(data),width=width,color="lightblue")
        for rec in rect:
            x = rec.get_x()
            height = rec.get_height()
            ax1.text(x+0.1, 1.001*height, str(height))

        xtick_list = [str(item) for item in df.index]
        ax1.set_xticks(x_bar)
        ax1.set_xticklabels(xtick_list)
        ax1.set_ylabel("sales")
        ax1.set_title("stock")
        ax1.grid(True)
        ax1.set_ylim(min(data)-10000, max(data)+10000)
        print xtick_list
        print data
        print min(data)
        print max(data)
        plt.xticks(rotation="89")
        plt.show()




if __name__ == '__main__':
       df = ts.get_cashflow_data(2014,3)

       print df.T
       # company =  Company("600688.csv")
       # company.bar()