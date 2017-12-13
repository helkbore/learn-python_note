#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'2017年12月8日'

import requests
import xml.etrrr.ElementTree as ET

def get_province_entry(url):

    content = requests.get(url).content.decode("gb2312")
    print(content)

provinces = get_province_entry("http://www.ip138.com/post/")