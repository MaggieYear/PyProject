#!/usr/bin/env python
#coding:utf-8
import urllib2
import re

#1、访问url，获取网页源代码
def spider_qiushi(url):

    user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(url=url, headers=headers)

    response = urllib2.urlopen(request)

    content = response.read()

    return content

#2、解析源代码，获取目标数据
def resolve_html(html_content):

    # 小点 .本身不包括换行符，re.S能让小点 .包括换行符
    #pattern = re.compile('<div class="content-text">(.*?)</div>', re.S)
    pattern = re.compile(r'<div class="content-text">.*?<span>(.*?)</span>.*?</div>', re.S)
    m = pattern.match(html_content)
    print( m )
    items = re.findall(pattern,html_content)
   # print items
   #  for item in items:
   #      print item

#3、保存数据


if __name__ == '__main__':
    url = "http://www.qiushibaike.com/textnew/page/1?s=4832451"
    content = spider_qiushi(url)
    #print(content)
    resolve_html(content)
    pass