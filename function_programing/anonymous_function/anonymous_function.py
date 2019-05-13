#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         anonymous_function
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

# lambda
print list(map(lambda x: x * x, [1, 2, 3]))
f = lambda x: x * x
print f(5)


# return lambda
def build(x, y):
	return lambda: x * x + y * y


f = build(3, 4)
print f()
