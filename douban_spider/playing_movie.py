#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mocha_kiki'
import urllib2
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

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



def nowplaying_movies(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    s = urllib2.urlopen(req)
    # print(s.read())
    parser = MovieParser()
    parser.feed(s.read())
    s.close()
    return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
    movies = nowplaying_movies(url)

    import json
    # 把字典转成json格式打印
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))
