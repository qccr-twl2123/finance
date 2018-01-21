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
        df = self.convert_csv_to_pd()
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
        ax1.set_ylim(min(data)-100000, max(data)+10000)
        print min(data)-100000
        print xtick_list
        print data
        print min(data)
        print max(data)
        plt.xticks(rotation="89")
        plt.show()

    def financial_analysis(object, year_list, code):
        net_profits_list = []
        index_list = []
        report_date_list = []
        for year in year_list:
            for m in range(3):
                index_list.append(str(year)+"-"+str(m+1))
                report_data = ts.get_report_data(year, m+1)
                report_data = report_data.set_index("code")
                report_data = report_data.ix[code]
                report_date_list.append(str(year)+report_data['report_date'])
                net_profits_list.append(report_data['report_date','net_profits'])

        summary = pd.DataFrame(index=index_list, columns=(['report_date', 'net_profits']))
        summary['net_profits'] = net_profits_list
        summary['report_date'] = report_date_list
        summary.to_csv(code+"_finance.csv",index=index_list,sep=',')



if __name__ == '__main__':
       # df = ts.get_report_data(2017,3)
       # df = df.set_index("code")
       # xs  = df.ix['600231']
       # print xs
       # print  '2017-'+xs['report_date']
       company =  Company("600688.csv")
       year_list = [2017]
       company.financial_analysis(year_list, '600231')

