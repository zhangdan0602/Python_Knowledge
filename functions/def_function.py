#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         def_function
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------
import math


# def
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x;


print my_abs(-99)


# pass
def nop():
	age = 22
	if age >= 18:
		pass
	else:
		print 'age > 18'


nop()


# return many value[tuple]
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y

r = move(200, 200, 30, math.pi / 3)
print r
