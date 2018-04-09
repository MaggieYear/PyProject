#!/usr/bin/env python
#coding:utf-8
import urllib2
import re
import os


class TeacherSpider(object):
    #构造方法
    def __init__(self):
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'

    # 1.先从url获取源代码
    def get_page(self,pageIndex):
        headers = {'User-Agent':self.user_agent}
        request = urllib2.Request(url=self.url%str(pageIndex),headers=headers)
        response = urllib2.urlopen(request)
        content = response.read()
        return content

    # 2.解析源代码获取教师姓名和介绍
    def analysis(self,content):
        #保存数据的文本
        main_info = ''
        teacher_name = ''
        teacher_info = ''

        # 解析出主要代码
        content_pattern = re.compile('<ul class="teacherList font12">(.*?)</ul>', re.S)
        content_items = re.findall(content_pattern, content)
        for main_content in content_items:
            content = main_content

        #解析出老师的主代码
        teacher_pattern = re.compile('<li class="t3out">(.*?)</li>', re.S)
        teacher_items = re.findall(teacher_pattern, content)
        for teacher in teacher_items:
            # 解析名字
            name_pattern = re.compile('<p.*?>(.*?)<a.*?href=.*?</a></p>', re.S)
            name_items = re.findall(name_pattern, teacher)
            for name in name_items:
                teacher_name =  name
                main_info += '名字：' + teacher_name + '\n'

            #解析介绍
            info_pattern = re.compile(' <p class="color66">.*?<span class="color99">.*?</span>(.*?)</p>', re.S)
            info_items = re.findall(info_pattern, teacher)
            for info in info_items:
                if info is '':
                    main_info += '简介：无'+ '\n'
                else:
                    teacher_info = info.replace('\n','')
                    main_info += '简介：' + teacher_info + '\n'

        return main_info

    # 3.保存数据
    def save(self,main_info,path,pageIndex):
        print '保存数据'
        #先处理一下需要保存的数据
        main_info = main_info.replace('&quot;',' ')
        if not os.path.exists(path):
            os.makedirs(path)
        #将每页的数据写到单独的文件
        #file_path = path + '/' + 'page_'+ str(pageIndex) + '.txt'
        #print file_path
        #将所有数据写到一个文件
        file_path = path + '/' + 'page'+ '.txt'

        f = open(file_path,'a+')
        f.writelines(main_info)
        f.close()

    # 4. 运行代码
    def run(self):
        print '开始抓取'
        spider = TeacherSpider()
        for pageIndex in range(1, 8): #28
            content = spider.get_page(pageIndex)
            main_info = spider.analysis(content)
            path = 'teachers'
            spider.save(main_info,path, pageIndex)

        print '抓取结束'

if __name__ == '__main__':
    spider = TeacherSpider()
    spider.run()






