#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'

# 从雅虎爬取股票数据
import urllib
import datetime

def download_stock_data(stock_list):

    for sid in stock_list:
        url = 'http://table.finance.yahoo.com/table.csv?s=' + sid
        fname = sid + '.csv'
        print('downloading %s form %s' % (fname, url))
        urllib.urlretrieve(url, fname)


def download_stock_data_in_period(stock_list, start, end):
    for sid in stock_list:
        params = {'a': start.month - 1, 'b': start.day, 'c': start.year,
                  'd': end.month - 1, 'e': end.dya, 'f': end.year, 's': sid}
        url = 'http://table.finance.yahoo.com/table.csv?'
        qs = urllib.urlencode(params)
        url = url + qs
        fname = '%s_%d%d%d_%d%d5d.csv' % (sid, start.year, start.month, start.day,
                                        end.year, end.month, end.day)
        print('downloading %s form %s' % (fname, url))
        urllib.urlretrieve(url, fname)


if __name__ == '__main__':
    stock_list = ['300001.sz', '300002.sz']
    start = datetime.date(year=2015, month=11, day=17)
    end = datetime.date(year=2015, month=12, day=17)
    # download_stock_data(stock_list)
    download_stock_data_in_period(stock_list, start, end)
