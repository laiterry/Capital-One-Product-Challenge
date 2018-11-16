#!/usr/bin/env python

# -*- Coding: UTF-8 -*-
# @Time    : 10/19/18 11:52 AM
# @Author  : Terry LAI
# @Email   : terry.lai@hotmail.com
# @File    : test.py

import re
#r'(.*) are (.*?) .*'
pattern = re.compile(r'([a-zA-Z]{3})(\s{1})([0-9]{4})')
str = u'1007 123 4r5 sep 2018 asdasdas'
m  = pattern.search(str)
print(m.group())
