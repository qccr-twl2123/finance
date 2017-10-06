#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

df=pd.read_csv("600871.csv")

# pd.DataFrame(columns=['open','close'])
#
# open = df["open"].T.values
# close = df["close"].T.values
# df['open'] = open
# df['close'] = close
#
df.plot()
plt.show()

