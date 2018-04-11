#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
from xml_utils import XmlUtils
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')
import time

"""
1、爬取麦子学院官网源代码
2、正则表达式取出第一级页面的url，保存到url_spider1,并写出到url1.xml文件
3、访问第一级页面获取的url，进入每个页面之后，再爬取url,保存到url_spider2,并写出到xml文件
4、遍历list2里的url，进入每个页面之后，再爬取url,保存到list3,并写出到url3.xml文件
"""

"""
优化方案
1、爬取麦子学院官网源代码
2、正则表达式取出第一级页面的url，保存到数据库表url_1,并写出到url1.xml文件
3、查询数据库表url_1，遍历每个url，进入每个页面之后，再爬取url,保存到数据库表url_2
4、查询数据库表url_2，遍历每个url进入每个页面之后，再爬取url,保存到数据库表url_3
5、查询数据库url_3,并写出到url3.xml文件，这就是所得的目标数据

6、增加定时抓取，对比数据库内容，保存更新的内容到数据表内，并保存抓取日志到数据表spider_log

"""

class UrlSpider:
    """根据url爬取连接，返回链接的列表"""
    def __init__(self,url,level):
        self.url = url
        self.level = level
        self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    #获取网页源代码
    @staticmethod
    def get_page(self):
        try:
            headers = {'User-Agent': self.user_agent}
            request = urllib2.Request(url=self.url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except :
            return None

    #解析源代码，获取url
    @staticmethod
    def analysis(self,content):
        list = []
        # 解析出所有url
        url_pattern = re.compile('href="(.*?)"', re.S)
        url_items = re.findall(url_pattern, content)

        count = 0
        for url in url_items:
            url = UrlSpider.dealWithUrl(self,url)
            if url is not None:
                count += 1
                list.append(url)
        return list

    #处理url，过滤掉不需要的
    @staticmethod
    def dealWithUrl(self,url):
        #判断url是否包含http://
        if 'http://' in url or 'https://' in  url :
            return url
        elif '/' in url :
            #/article/28693/,拼接url
            url = self.url + url
            return url
        else:
            #javascript:void(null) --> js需要过滤掉
            return None

    def spiderRun(self):
        content = UrlSpider.get_page(self)
        if content is not None:
            return UrlSpider.analysis(self,content)
        else:
            return None

    #保存list数据到xml文件
    def saveToXml(self,list,path,filename):
        #list 转 字典
        dict = {}
        index_key = 0
        for url in list:
            base_dict = {}
            base_dict['loc'] = url
            base_dict['lastmod'] = '2014-08-08T01:10:39+00:00'
            base_dict['changefreq'] = 'weekly'
            base_dict['priority'] = '0.3'
            dict[index_key] = base_dict
            index_key += 1

        xmlUtils = XmlUtils()
        root = xmlUtils.urlmap_to_xml(dict, 'urlset', 'url')  # 将dict转换为xml
        xmlUtils.out_xml(root, path, filename)  # 输出xml到out_files

class SpiderExecute:
    """执行爬虫爬取的类"""

    def goto_spider(self):
        # 一级链接
        url = "http://www.maiziedu.com"
        urlSpider = UrlSpider(url, 1)
        # 二级链接
        url_list = urlSpider.spiderRun()

        if url_list is not None:
            # 将url列表保存到xml文件
            path = "url_spider1"
            filename = "url1.xml"
            urlSpider.saveToXml(url_list, path,filename)

            url_set = set()
            count = 0
            index = 0
            # 三级链接
            for url in url_list:
                if url is not None:
                    print ">>"
                    urlSpider = UrlSpider(url, 2)
                    index += 1
                    # 三级链接
                    _url_list = urlSpider.spiderRun()
                    # 将url列表保存到xml文件
                    path = "url_spider2"
                    filename = "url"+str(index)+".xml"
                    if _url_list is not None:
                        try:
                            urlSpider.saveToXml(_url_list, path, filename)
                        except:
                            print "出错父url：" + url
                        for _url in _url_list:
                            if _url is not None:
                                url_set.add(_url)
                        count += len(url_set)

            print '父url数量:' + str(index)  #--两百多条
            print '子url数量:' + str(count)  #--数量多达百万，如果这能变现就好了，完全发家致富嘛(´-ι_-｀)

            # 将url列表保存到数据库
            #尚未实现！

if __name__ == '__main__':
    start = time.clock()  # 记录处理开始时间；与最后一行一起使用，来判断输出运行时间。
    spiderExecute = SpiderExecute()
    spiderExecute.goto_spider()
    end = time.clock()
    print("read: %f s" % (end - start))