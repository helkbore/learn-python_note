#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'爬取 2017年12月4日'
import requests
from bs4 import BeautifulSoup
import random
import book_db

# -- 公共方法
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

# -- 爬取集思会
# ---- 爬取集思会书籍分类



def get_jsh_type():
    url = "http://www.kindlepush.com/category"

    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    bl_ul = soup.find("ul", attrs={'class': 'w-list'})
    liTags = bl_ul.find_all('a')
    # print(liTags)

    for l in liTags:
        type = {}
        type['name'] = l.text.strip()
        type['href'] = l["href"]
        # print(type)
        book_db.save_book('book_type', type)

get_jsh_type()