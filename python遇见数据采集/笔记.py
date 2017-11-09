#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'笔记 2017年11月6日'

__author__ = 'Gentiana'

# urllib
'''
Python 3.x中提供的一系列操作URL的库
'''

# urllib 使用步骤
'''
导入urllib库
    from urllib import request
请求URL
    resp = request.urlopen('http://www.baidu.com')
使用相应对象输出数据
    print(resp.read().decode("utf-8"))
'''