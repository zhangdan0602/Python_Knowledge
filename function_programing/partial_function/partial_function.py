#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         partial_function
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

import functools

print int('12345')

# binary converse
print int('12345', base=8)
print int('12345', 16)


def int2(x, base=2):
	print '---'
	return int(x, base)


print int2('10000101')

int2 = functools.partial(int, base=2)
print int2('10000')

print '---------------'
max2 = functools.partial(max, 100)
# args = (100, 32, 10, 99)
print max2(22, 101, 99)

args = (32, 10, 99)
print max2(*args)
