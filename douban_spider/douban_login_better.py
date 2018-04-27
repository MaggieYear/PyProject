#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import requests
from PIL import Image

# 登录
def get_captcha(url, headers):
    data = {    # 传输数据
        'source': None,
        'redir': 'https://www.douban.com/people/168341339/',
        'form_email': '380075669@qq.com',
        'form_password': 'Geren123+-',
        'login': '登录'
        #'captcha-solution': '',
        #'captcha-id': ''
        }

    # req = requests.get(url=url, headers=headers)
    # info = req.text

    # html = etree.HTML(info)     # 获取验证码链接和ID
    # captcha_solutions = html.xpath('//div[@class="item item-captcha"]/div/img/@src')
    # data['captcha-id'] = html.xpath('//input[@name="captcha-id"]/@value')
    # print(len(captcha_solutions))
    # img = requests.get(captcha_solutions[0])
    # with open('1.jpg', 'wb') as f:
    #         f.write(img.content)
    # im = Image.open('1.jpg')
    # im.show()
    # data['captcha-solution'] = input('请输入验证码：')

    session = requests.Session()
    resp = session.post(url, data=data, headers=headers)
    print(resp.content)
    return session

# 获得主页的源代码
def get_myindex(url, session):
    req = session.get(url)
    html = req.text
    print(html)

# 修改个人签名
def edit_signature(url, signature, session, ck='PvCf'):
    r = session.get(url)
    headers = {'Referer': url,
                'Host': 'www.douban.com',
                'X - Requested - With': 'XMLHttpRequest'}
    data = {'ck': ck, 'signature': signature}
    r = session.post(url, data=data, headers=headers)
    print(r.content)


if __name__ == '__main__':

    url = 'https://www.douban.com/accounts/login'

    agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    headers = {'User-Agent': agent}

    session = get_captcha(url, headers)
    my_url = 'https://www.douban.com/people/168341339/'
    # 打开我的主页
    get_myindex(my_url, session)

    # 修改个人签名
    username = '168341339'
    signature = '现实不似我所见'
    edit_sign_url = 'https://www.douban.com/j/people/' + username + '/edit_signature'
    edit_signature(edit_sign_url, signature. session)


#
# print(resp.text)

# print(captcha_solutions)







