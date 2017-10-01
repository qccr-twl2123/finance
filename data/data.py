import tushare as ts

df = ts.get_hist_data('600871')
df.to_csv('/Users/mark1xie/test/600871.csv')