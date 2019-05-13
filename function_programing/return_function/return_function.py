#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         return_function
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

# return
def cal_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax


nums = [1, 2, 3]
print cal_sum(*nums)


def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax

	return sum


print lazy_sum(nums)
print lazy_sum((1, 2, 3))


def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i

		fs.append(f)
	return fs


f1, f2, f3 = count()
print f1(), f2(), f3()


def count1():
	def f(j):
		def g():
			return j * j

		return g

	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs


f1, f2, f3 = count1()
print f1(), f2(), f3()
