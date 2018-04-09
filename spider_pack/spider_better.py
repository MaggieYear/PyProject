#!/usr/bin/env python
#coding:utf-8
import urllib2
import re
import os


class Spider(object):

    # 构造方法
    def __init__(self):
        self.url = "http://www.qiushibaike.com/textnew/page/%s?s=4832451"
        self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    # 1、访问url，获取网页源代码
    def get_page(self,pageIndex):

        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url=self.url%str(pageIndex), headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()

    # 2、解析源代码，获取目标数据
    def analysis(self,content):
        # 小点 .本身不包括换行符，re.S能让小点 .包括换行符
        pattern = re.compile(r'<div class="content-text">.*?<span>(.*?)</span>.*?</div>', re.S)
        items = re.findall(pattern, content)
        print len(items)
        return items

    #3、保存数据
    def save(self,items,path,pageIndex):
        count = 1
        for item in items:
            # print item

            # 把多余的换行符去掉'\n'
            # 把<br/>换成换行符'\n'
            item_new = item.replace('\n', '').replace("<br/>", '\n')

            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + str(count) + '.txt'
            f = open(file_path, 'w')
            f.write(item_new)
            f.close()
            count += 1

    # 4、运行的方法
    def run(self):
        print '开始抓取'
        for i in range(1, 5):
            # 获取网页源代码
            content = self.get_page(i)
            # print(content)
            # 解析源代码获取数据
            items = self.analysis(content)
            path = 'qiushibaike_' + str(i)
            self.save(items,path,i)
        print '抓取结束'


if __name__ == '__main__':
    spider = Spider()
    spider.run()