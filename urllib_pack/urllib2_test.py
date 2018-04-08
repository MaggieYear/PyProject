#!/usr/bin/env python
import urllib
import urllib2


def source_html():
    url = "https://www.qiushibaike.com/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}

    request = urllib2.Request(url=url, headers=headers)

    response = urllib2.urlopen(request)

    print response.read()

def login_request():
    url = "http://www.maiziedu.com/user/login/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}

    values = {'account_l':'18682268349','password_l':'eqqweqw'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url=url,data=data, headers=headers)

    response = urllib2.urlopen(request)

    print response.read()

if __name__ == '__main__':
    #source_html()
    login_request()
