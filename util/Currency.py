#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import sys
import ffn
import numpy as np
from scipy.stats import norm
reload(sys)
sys.setdefaultencoding('utf-8')

df = ts.get_money_supply()
# print df.head(5)
dates = df['month'].T.values
m2 = df['m2'].T.values
m2 = [float(x) for x in m2]
dates = [str(x).replace(".", "-") for x in dates]
print dates
print m2
plt.plot(dates, m2)
plt.show()