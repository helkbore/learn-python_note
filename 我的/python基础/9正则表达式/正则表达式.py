#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'正则表达式 2017年11月20日'

# re模块
import re

# 判断是否匹配
re.match(r'\d{3}\-\d{3,8}$', '010-12345')
print(re.match(r'\d{3}\-\d{3,8}$', '010-12345'))

'''
match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
'''

