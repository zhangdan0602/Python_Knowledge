#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         recruise
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------

# recurse
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)


print fact(5)


def fact1(n):
	return fact_iter(n, 1)


def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)


print fact1(10)

def move(n, a, b, c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1, a, b, c)
		move(n-1,b,a,c)
move(3, 'A', 'B', 'C')
