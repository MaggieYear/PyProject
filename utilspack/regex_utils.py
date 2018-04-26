#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import re

def re_demo():
    # 解析价格
    txt = 'If you purchase more than 100 sets,the price of product A is $9.90.'
    # 解析数量和价格：
    m = re.search(r'(\d+).*\s(\d+\.?\d*)', txt)
    print(m.)
    print(m.groups())

if __name__ == '__main__':
    re_demo()