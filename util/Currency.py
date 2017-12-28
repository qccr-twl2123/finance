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
print type(df)
print df
# plt.plot(m2)
# plt.show()