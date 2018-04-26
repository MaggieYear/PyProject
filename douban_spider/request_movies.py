#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import urllib2
import requests
from HTMLParser import HTMLParser
import os

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        # 正在上映的电影data-category=nowplaying
        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs, 'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['release'] = _attr(attrs, 'data-release')
            movie['duration'] = _attr(attrs, 'data-duration')
            movie['region'] = _attr(attrs, 'data-region')
            movie['directors'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            movie['star'] = _attr(attrs, 'data-star')
            movie['category'] = _attr(attrs, 'data-category')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(release)s|%(duration)s|%(region)s|%(directors)s|%(actors)s|%(star)s|%(category)s|' % movie)
            self.in_movies = True
        # 获取图片链接
        if tag == 'img' and self.in_movies:
            self.in_movies = False
            src = _attr(attrs, 'src')
            movie = self.movies[len(self.movies) - 1]
            movie['poster-url'] = src
            _download_poster_image(movie)

# 从url下载图片
def _download_poster_image(movie):
    src = movie['poster-url']
    # 忽略证书下载图片
    r = requests.get(src, verify=False)
    # 下载到img文件夹下
    path = 'img'
    if not os.path.exists(path):
        os.makedirs(path)

    fname = src.split("/")[-1]
    file_path = path + '/' + fname
    print(file_path)
    # 二进制写出到文件
    with open(file_path, 'wb') as f:
       f.write(r.content)
       movie['poster-path'] = file_path

def nowplaying_movies(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    r = requests.get(url, headers=headers)
    parser = MovieParser()
    parser.feed(r.content)
    return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    movies = nowplaying_movies(url)

    import json
    # 把字典转成json格式打印
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))
