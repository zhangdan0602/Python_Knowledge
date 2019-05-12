#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         iterate
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------

from collections import Iterable

# list
l = ['mike', 'sarah', 'bob', 'jack']
for i in l:
	print i
for i, value in enumerate(l):
	print i, value

# dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key;

for value in d.values():
	print value

for item in d.items():
	print item
for key, value in d.items():
	print key, value

# str
str = 'abc'
for c in str:
	print c

print isinstance('123', Iterable)
print isinstance(123, Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance((1, 2, 3), Iterable)
print isinstance(d, Iterable)

# set
s = [(1, 2), (3, 4), (5, 6)]
for x, y in s:
	print x, y
