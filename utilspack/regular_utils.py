#!/usr/bin/env python
#coding:utf-8

import re

#1、判断字符串是否全部是小写字母
def is_lower_case():
    str1 = 'dsdkjfsldkf'
    an = re.match('[a-z]+$',str1)
    if an:
        print '全是小写'
    else:
        print '全是大写'

#2、判断是否存在小写
def search_def():
    str1 = 'dsdkjDsldkf'
    an = re.search('^[a-z]+$',str1)
    if an:
        print '全是小写'
    else:
        print '有大写'

#3、编译正则表达式
def compile_def():
    str1 = 'dsdkjDsldkf'
    regex = re.compile('^[a-z]+$')
    an = regex.search(str1)
    if an:
        print '全是小写'
    else:
        print '有大写'

#4、提取分组的字符串，数字和字母分组
def group_def():
    str1 = '32142dfsdf1231cdfg'
    obj = re.search('([0-9]+)([a-z]+)([0-9]+)([a-z]+)',str1)
    print obj.group()  #32142dfsdf1231cdfg
    print obj.group(0)  #32142dfsdf1231cdfg
    print obj.group(1)  #32142
    print obj.group(2)    #dfsdf
    print obj.group(3)    #1231
    print obj.group(4)    #cdfg

def phone_regex():
    str1 = '这个18685244349是一个手机号，18672883726也是手机号'
    #  ?:  不分组
    regex_phone = re.compile('((?:(?:13[0-9])|(?:15[^4,\D])|(?:18[0,2,5-9]))\d{8})')
    print regex_phone.findall(str1)

if __name__ == "__main__":

    #search_def()
    #compile_def()
    #group_def()

    phone_regex()
