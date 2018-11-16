#!/usr/bin/env python

# -*- Coding: UTF-8 -*-
# @Time    : 11/15/18 4:19 PM
# @Author  : Terry LAI
# @Email   : terry.lai@hotmail.com
# @File    : readline.py

import fileinput

f1 = open('a.txt', 'r')
f2 = open('b.txt', 'w') # 若是'wb'就表示写二进制文件
for line in f1:
    f2.write(',\''+line.strip()+'\'')
f1.close()
f2.close()

