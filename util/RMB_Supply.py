#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class RmbSupply(object):

    def __init__(self,year_list):
        self.__year_list = year_list

    def covert_to_data_frame(self, year):

        df = pd.read_csv(year+"_RMB_SUPPLY.csv",index_col="Item")
        dates = pd.to_datetime(df.T.index)
        m0_1 = df.T["M0"].values
        m1_1 = df.T["M1"].values
        m2_1 = df.T["M2"].values
        m0 = [m0_1[i] for i in range(len(m0_1)) if np.isnan(m0_1[i]) == False]
        m1 = [m1_1[i] for i in range(len(m1_1)) if np.isnan(m1_1[i]) == False]
        m2 = [m2_1[i] for i in range(len(m2_1)) if np.isnan(m2_1[i]) == False]

        # 将csv 转换成表转DateFrame格式数据
        m_pd = pd.DataFrame(index=dates, columns=(['m0','m1','m2']))
        m_pd['m0'] = m0
        m_pd['m1'] = m1
        m_pd['m2'] = m2
        return m_pd

    def contact_data(self):
        year_data_list = []
        for year in self.__year_list:
            year_data_list.append(self.covert_to_data_frame(year))

        df = pd.concat(year_data_list,ignore_index=False)
        return df

    def calculate_growth_rate(self):
        df = self.contact_data()
        df["m0增长率"] = (df["m0"] - df["m0"].shift(-1))/df["m0"]
        df['m0增长率'].fillna(value=0, inplace=True)
        df["m1增长率"] = (df["m1"] - df["m1"].shift(-1))/df["m1"]
        df['m1增长率'].fillna(value=0, inplace=True)
        df["m2增长率"] = (df["m2"] - df["m2"].shift(-1))/df["m2"]
        df['m2增长率'].fillna(value=0, inplace=True)
        return df

    def generate_analysis_hist_chart(self):
        df = self.calculate_growth_rate()
        show_data_list = df['m0增长率'].T.values
        print show_data_list
        plt.hist(show_data_list,bins=12)
        plt.title("m0增长率")
        plt.show()

    def generate_analysis_trend_chart(self):
        df = self.calculate_growth_rate()
        x = pd.to_datetime(df.index,format="%Y-%m-%d")
        y = df['m0增长率'].T.values
        plt.plot(x, y, label="m0增长率",color="r")
        plt.show()

    def generate_analysis_scatter_chart(self):

        df = self.calculate_growth_rate()
        print df
        m0 = df["m0增长率"]
        m1 = df["m1增长率"]
        m2 = df["m2增长率"]
        plt.scatter(m0, m2, color="r")
        plt.show()

if __name__=="__main__":
     year_list = ["2015","2016","2017"]
     rmb_supply = RmbSupply(year_list)
     rmb_supply.generate_analysis_scatter_chart()

