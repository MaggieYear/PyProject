#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import re

def re_demo():
    # 解析价格
    txt = 'If you purchase more than 100 sets,the price of product A is $9.90.'
    # 解析数量和价格：
    m = re.search(r'(\d+).*\$(\d+\.?\d*)', txt)
    print(m.groups())

# re匹配方法使用示例
def re_method():
    # search vs match
    s1 = 'abcd'
    print(re.search(r'c', s1))
    print(re.search(r'^c', s1))   # None
    print(re.match(r'.*c', s1))  # <_sre.SRE_Match object at 0x02F2A758>

    # split
    s2 = 'This is a long string'
    print(re.split(r'\W', s2))  # ['This', 'is', 'a', 'long', 'string']

    s4 = 'If you purchase more than 100 sets,the price of product A is $9.90.'

    # findall
    # 找出所有单词
    print(re.findall(r'\w+', s2))
    # 找出所有数字
    print(re.findall(r'\d+', s4))  # ['100', '9', '90']
    print(re.findall(r'\d+\.?\d*', s4))  # ['100', '9.90']

    # finditer
    items = re.finditer(r'\d+\.?\d*', s4)
    for item in items:
        print(item.group())  # 100  9.90

    # 替换字符串
    print(re.sub(r'\d+\.?\d*', '<number>', s4))
    # If you purchase more than <number> sets,the price of product A is $<number>.

    # 替换字符串，并返回替换的个数
    print(re.subn(r'\d+\.?\d*', '<number>', s4))
    # ('If you purchase more than <number> sets,the price of product A is $<number>.', 2)

    # 匹配分组
    s5 = 'mocha kiki is a little girl'
    m = re.match(r'\w+ (\w+) (\w+)', s5)
    print(m.group(0))  # mocha kiki is
    print(m.group(1))  # kiki
    print(m.group(0, 1, 2))  # ('mocha kiki is', 'kiki', 'is')
    print(m.groups())  # 返回从匹配项开始的字符串('kiki', 'is')

# 正则表达式语法规则
def regex_grammer():
    # dot 点  '.'任意字符
    print(re.match(r'.', 'abc\nsdfksd').group())  # 匹配任意字符一个 -->a
    # 匹配个数
    print('匹配个数')
    # '*'匹配0个或多个
    print(re.match(r'.*', 'abc\nsdfksd').group())  # abc  遇到换行符结束了
    print(re.match(r'.*', 'abc\nsdfksd', re.DOTALL).group())  # 点包含所有符号 abc sdfksd
    # '+'匹配1个或多个
    print(re.match(r'ab?', 'abbdsdf\nabsdfksd').group())
    # '?'匹配0个或1个
    print('匹配字符串开头')
    # 匹配字符串开头
    print(re.findall(r'^abc', 'abc\nabc'))  # ['abc'] 这个字符串相当于两行，只匹配了一行
    # 匹配多行字符串
    print(re.findall(r'^abc', 'abc\nabc', re.MULTILINE))  # ['abc', 'abc']

    # '$' 匹配字符串结尾
    print(re.findall(r'abc\d$', 'abc1\nabc2'))  # ['abc2']
    print(re.findall(r'abc\d$', 'abc1\nabc2', re.MULTILINE))  # ['abc1', 'abc2']

    # 匹配个数


if __name__ == '__main__':
    regex_grammer()