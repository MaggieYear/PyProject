#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import requests

def get_json(url):
    r = requests.get(url)
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.text)
    print(r.json())

def get_querystring(url):
    params = {'qs1': 'value1', 'qs2': 'value2'}
    headers = {'x-hearder1': 'value1','x-header2': 'value2'}
    r = requests.get(url,params=params,headers=headers)
    print(r.status_code)
    print(r.content)

def get_cookie(url):
    headers = {'User-Agent': 'Chrome'}
    r = requests.get(url,headers=headers)
    print(r.status_code)
    print(r.cookies)
    print(r.cookies['bid'])
    print(r.cookies['ll'])


if __name__ == '__main__':
    url = 'https://api.github.com/events'
    # get_json(url)

    http_bin = 'http://httpbin.org/get'
    # get_querystring(http_bin)

    douban_url = 'http://www.douban.com'
    get_cookie(douban_url)