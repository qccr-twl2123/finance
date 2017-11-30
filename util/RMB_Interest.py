#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
import tushare as ts
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

df = ts.get_loan_rate()
print df.head()
rate_df = pd.DataFrame(index=df[df.loan_type == '短期贷款(六个月以内)']['date'],
                       columns=['短期贷款(六个月以内)','短期贷款(六个月至一年)','中长期贷款(三至五年)','中长期贷款(五年以上)'])


rate_df['短期贷款(六个月以内)'] = [float(x) for x in df[df.loan_type == '短期贷款(六个月以内)']['rate'].T.values]
rate_df['短期贷款(六个月至一年)'] = [float(x) for x in df[df.loan_type == '短期贷款(六个月至一年)']['rate'].T.values]
rate_df['中长期贷款(三至五年)'] = [float(x) for x in df[df.loan_type == '中长期贷款(三至五年)']['rate'].T.values]
rate_df['中长期贷款(五年以上)'] = [float(x) for x in df[df.loan_type == '中长期贷款(五年以上)']['rate'].T.values]

print rate_df.head()

x = pd.to_datetime(rate_df.index,format="%Y-%m-%d")
y = rate_df['短期贷款(六个月以内)'].T.values
z = rate_df['短期贷款(六个月至一年)'].T.values
m = rate_df['中长期贷款(三至五年)'].T.values

plt.plot(x, y, label="短期贷款(六个月以内)",c="red")
plt.plot(x, z, label="短期贷款(六个月至一年)",c="green")
plt.plot(x, m, label="中长期贷款(三至五年)",c="black")
plt.legend()
plt.xlabel("日期")
plt.ylabel("利率")
plt.xticks(rotation="45")
plt.show()


