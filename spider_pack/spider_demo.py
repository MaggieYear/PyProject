#!/usr/bin/env python
#coding:utf-8
import urllib2
import re
import os

#1、访问url，获取网页源代码
def spider_qiushi(url):
    user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib2.Request(url=url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read()
    except urllib2.HTTPError as e:
        print e
        exit()
    except urllib2.URLError as e:
        print e
        exit()
    return content


#2、解析源代码，获取目标数据
def resolve_html(html_content,index):

    # 小点 .本身不包括换行符，re.S能让小点 .包括换行符
    pattern = re.compile(r'<div class="content-text">.*?<span>(.*?)</span>.*?</div>', re.S)
    items = re.findall(pattern,html_content)
    print len(items)
    count = 1
    for item in items:
       # print item

       #把多余的换行符去掉'\n'
       #把<br/>换成换行符'\n'
        item_new = item.replace('\n','').replace("<br/>",'\n')

       # 3、保存数据
        path = 'qiushibaike_'+str(index)
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = path + '/' + str(count) +'.txt'
        f = open(file_path,'w')
        f.write(item_new)
        f.close()
        count += 1


if __name__ == '__main__':
    print '开始抓取'
    for i in range(1,5):
        url = "http://www.qiushibaike.com/textnew/page/" + str(i) + "?s=4832451"
        #获取网页源代码
        content = spider_qiushi(url)
        #print(content)
        #解析源代码获取数据
        resolve_html(content,i)
    print '抓取结束'