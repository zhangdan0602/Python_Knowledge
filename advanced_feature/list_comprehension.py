#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         list_comprehension
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------
import os

print list(range(1, 11))
# one loop
print [x * x for x in range(1, 11)]
# one loop and condition
print [x * x for x in range(1, 11) if x % 2 == 0]
# two loop
print [m + n for m in 'abc' for n in 'efg']
print [d for d in os.listdir('.')]
# get list
d = {'a': '1', 'b': '2', 'c': '3'}
print [k + '=' + v for k, v in d.items()]

# lower
l = ['HELLO','WORLD','C+']
print [s.lower() for s in l]
