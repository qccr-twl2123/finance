#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class RmbSupply(object):

    def __init__(self,year):
        self.__year = year

    def generate_analysis_chart(self):
        df = pd.read_csv(self.__year+"_RMB_SUPPLY.csv",index_col="Item")
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
        print m_pd



if __name__=="__main__":
     rmb_supply = RmbSupply("2017")
     rmb_supply.generate_analysis_chart();