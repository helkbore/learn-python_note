#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'知乎-从零开始写爬虫-笔记-1.5获取百度贴吧内容 2017年11月6日'

__author__ = 'Gentiana'

'''
网址: http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%B5%E5%AD%90%E4%B9%A6&fr=search
python: 3.6
lxml, BeautifulSoup

目标:
1. 从网上爬下特定页码的网页
2. 对于爬下的页面内容进行简单的筛选分析
3. 找到每一篇帖子的 标题、发帖人、日期、楼层、以及跳转链接
4. 将结果保存到文本。
'''

import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "

def get_content(url):
    comments = []

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')

    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    return liTags

url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E7%94%B5%E5%AD%90%E4%B9%A6&fr=search'
print(get_content(url))