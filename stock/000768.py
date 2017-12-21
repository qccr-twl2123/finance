#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tushare as ts
import matplotlib.pyplot as plt
import  pandas as pd
from scipy import stats
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class zhongHangFeiJi(object):

    def __init__(self, code):
        self.code = code




if __name__ == '__main__':
    zhongHangFeiJi = zhongHangFeiJi("00768")
