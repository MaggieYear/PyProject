# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup
import lxml
url = 'http://www.autohome.com.cn/3307/'

response = urllib2.urlopen(url)

soup = BeautifulSoup(response.read(), 'lxml')

print soup.find_all('div', 'car_navigate')