#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         map_reduce
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

from functools import reduce


# abstract
# map
def f(x):
	return x * x


r = map(f, [1, 2, 3])
print list(r)
print list(map(str, [1, 2, 3, 4, 5]))


# reduce
def add(x, y):
	return x + y


print reduce(add, [1, 3, 5, 7, 9])


def fn(x, y):
	return x * 10 + y


print reduce(fn, [1, 3, 5, 7])


def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '5': 5, '6': 6, '7': 7, '9': 9}
	return digits[s]


print reduce(fn, map(char2num, '13579'))

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '5': 5, '6': 6, '7': 7, '9': 9}


def str2int(s):
	def fn(x, y):
		return x * 10 + y

	def char2num(s):
		return digits[s]

	return reduce(fn, map(char2num, s))


print str2int('13579')


# lambda
def char2num2(s):
	return digits[s]


def str2int2(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num2, s))


print str2int2('13579')
