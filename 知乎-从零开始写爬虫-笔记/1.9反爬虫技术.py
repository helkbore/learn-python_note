#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'练习-抓取王者荣耀-英雄,金币等 2017年11月10日'

__author__ = 'Gentiana'

import requestshttp://113.230.76.170:5333/WebReport/ReportServer?reportlet=zsfxck/20w/20wjs.cpt&op=write&stime=&endtime=&gh=system&userid=40288d9e58425bc8015842649c580005&username=%E
from bs4 import BeautifulSoup
import random

# 从一系列的user-agent里随机挑出一个符合标准的使用
agents = []
fakeheader = {}
fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
