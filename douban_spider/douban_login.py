#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import requests
from HTMLParser import HTMLParser
import os
import time

class DoubanClient(object):

    def __init__(self):
        object.__init__(self)
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
                   'Origin': 'https://accounts.douban.com'}
        self.session = requests.Session()
        self.session.headers.update(headers)

    def login(self, url, username, password, source='None',
              redir='https://www.douban.com/'):
        r = self.session.get(url)

        # 如果有验证码的话，获取验证码
        (captcha_id, captcha_url) = _get_captcha(r.content)
        if captcha_id:
            captcha_solution = raw_input('enter solution for [%s]:' % captcha_url)

        data = {'source': source,
                'redir': redir,
                'form_email': username,
                'form_password': password,
                'login': '登录'}
        if captcha_id:
            data['captcha-id'] = captcha_id
            data['captcha-solution'] = captcha_solution

        headers = {'Referer': 'https://accounts.douban.com/login',
                   'Host': 'accounts.douban.com'}

        req = self.session.post(url, data=data, headers=headers, verify=False)
        # 登录成功后返回的cookies
        print(self.session.cookies.items())
        # print(req.content)

    # 修改个人签名
    def edit_signature(self, username, signature, ck='PvCf'):
        pre_url = 'https://www.douban.com/people/%s' % username
        r = self.session.get(pre_url)
        # ck = _get_ck(r.content)
        ck = _attr(self.session.cookies.items(), 'ck')

        url = 'https://www.douban.com/j/people/%s/edit_signature' % username
        headers = {'Referer': pre_url,
                'Host': 'www.douban.com',
                'X - Requested - With': 'XMLHttpRequest'}
        data = {'ck': ck, 'signature': signature}
        r = self.session.post(url, data=data, headers=headers, verify=False)

def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

# 获取验证码
def _get_captcha(content):

    class CaptchaParser(HTMLParser):
        def __int__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_url = None

        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'captcha-id':
                self.captcha_id = _attr(attrs, 'value')

            if tag == 'img' and _attr(attrs, 'id') == 'captcha_image' and _attr(attrs, 'class') == 'captcha_image':
                self.captcha_url = _attr(attrs, 'src')
                # _download_image(self.captcha_url)

    p = CaptchaParser()
    p.feed(content)
    return p.captcha_id, p.captcha_url

# 从url下载图片
def _download_image(url):
    # 忽略证书下载图片
    r = requests.get(url, verify=False)
    # 下载到img文件夹下
    path = 'captcha'
    if not os.path.exists(path):
        os.makedirs(path)
    cur_time = time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
    fname = cur_time + ".jpg"
    file_path = path + '/' + fname
    print(file_path)
    # 二进制写出到文件
    with open(file_path, 'wb') as f:
       f.write(r.content)

# 获得个人签名的表单，修改个人签名
def _get_ck(content):

    class CKParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.ck = None

        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs, 'type') == 'hidden' and _attr(attrs, 'name') == 'ck':
                self.ck = _attr(attrs, 'value')

    p = CKParser()
    p.feed(content)
    return p.ck

if __name__ == '__main__':
    # url = 'https://www.douban.com/accounts/login'
    url = 'https://accounts.douban.com/login'
    c = DoubanClient()
    c.login(url, 'xxxxx', 'xxxxx')

    user_id = 'xxxxxx'
    signature = '听风不是雨'
    c.edit_signature(user_id, signature)
