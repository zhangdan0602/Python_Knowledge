#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         filter
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

# filter
def is_odd(n):
	return n % 2 == 1


print list(filter(is_odd, [1, 2, 3, 4, 5, 6]))


def not_empty(s):
	return s and s.strip()


print list(filter(not_empty, ['a', '', 'b', ' ', None]))


def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n


def _not_divisible(n):
	return lambda x: x % n > 0


def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)


for n in primes():
	if n < 10:
		print n
	else:
		break
