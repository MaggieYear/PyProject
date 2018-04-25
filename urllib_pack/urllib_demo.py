#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'

import urllib
import urlparse

def urlencode():
    params = {'score': 100, 'name': '爬虫基础', 'comment': 'very good'}
    # url编码
    encode_param = urllib.urlencode(params)
    print(encode_param)
    # comment=very+good&score=100&name=%E7%88%AC%E8%99%AB%E5%9F%BA%E7%A1%80
    # url解码
    parse_code = urlparse.parse_qs(encode_param)
    print(parse_code)
    # {'comment': ['very good'], 'score': ['100'], 'name': ['\xe7\x88\xac\xe8\x99\xab\xe5\x9f\xba\xe7\xa1\x80']}

    # 分解url
    url = 'https://baike.baidu.com/tashuo/browse/content?id=7225f0f4a7ec283da39a73c7&fr=qingtian&lemmaId=4815748'
    result = urlparse.urlparse(url)
    print(result)
    # ParseResult(scheme='https', netloc='baike.baidu.com', path='/tashuo/browse/content', params='', query='id=7225f0f4a7ec283da39a73c7&fr=qingtian&lemmaId=4815748', fragment='')
    param = urlparse.parse_qs(result.query)
    print(param)

if __name__ == '__main__':
    # demo()
    # retrieve()
    urlencode()


def print_list(lines):
    for i in lines:
        print(i)

def demo():
    s = urllib.urlopen('http://blog.kamidox.com')
    # lines = s.readlines()
    # print_list(lines)
    # 打印返回码
    # print(s.getcode())

    # HttpMessage实例
    msg = s.info()
    # 打印头部信息
    # print_list(msg.headers)
    # 打印头部信息（元组格式）
    # print_list(msg.items())
    # 获得头部某个字段数据
    # print(msg.getheader('content-length'))

def progress(blk, blk_size, total_size):
    print('%d/%d - %.02f' % (blk * blk_size, total_size, (float)(blk * blk_size) * 100 / total_size))
    pass

def retrieve():
    fname, msg = urllib.urlretrieve('http://blog.kamidox.com', 'index.html', reporthook=progress)
    print(fname)  # index.html
    #print_list(msg.items())

