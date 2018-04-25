#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import urllib
import urllib2
import cookielib

def urlopen(url):

    try:
        s = urllib2.urlopen(url, timeout=3)
    except urllib2.HTTPError, e:
        print(e)
    else:
        print(s.read(100))
        s.close()

def request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    s = urllib2.urlopen(req)
    print(s.read(100))
    s.close()

# 安装默认的opener，系统会自动用opener打开链接
def install_opener():
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),
                                  urllib2.HTTPSHandler(debuglevel=1))
    urllib2.install_opener(opener)

def opener(url):
    data = { 'username': 'xxxxxxx', 'password': "xxxxxx"}
    headers = { 'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(url, data=urllib.urlencode(data), headers=headers)
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    s = opener.open(req)
    print(s.read100)
    s.close

def handle_cookie(url):
    cookiejar = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler(debuglevel=1))
    s = opener.open(url)
    print(s.read(100))
    s.close()

    print('=' * 80)
    print(cookiejar._cookies)
    print('=' * 80)

    s = opener.open(url)
    s.close()

if __name__ == '__main__':
    url = 'http://blog.kamidox.com/'
    #install_opener()
    #request(url)

    # urlopen(url)
    douban_url = 'http://www.duoban.com'
   # opener(douban_url)
    handle_cookie(douban_url)