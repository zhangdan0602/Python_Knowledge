#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         process_error
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

import logging


def foo():
	r = some_function()
	if r == (-1):
		return (-1)
	return r


def some_function():
	pass


# try catch
try:
	print 'try..'
	r = 10 / 0
	print 'rs:%s', r
except ZeroDivisionError as e:
	print 'except:%s' % e
finally:
	print 'finally'
print 'end'

try:
	print 'try..'
	r = 10 / int('a')
	print 'rs:%s', r
except ValueError as e:
	print 'ValueError:', e
except ZeroDivisionError as e:
	print 'Zero:', e
finally:
	print 'finally'
print 'end'

try:
	foo()
except ValueError as e:
	print 'ValueError'
#  son class
except UnicodeError as e:
	print 'UnicodeError'

print '------'


def foo(s):
	return 10 / int(s)


def bar(s):
	return foo(s) * 2


def main():
	try:
		bar('0')
	except Exception as e:
		# logging.exception(e)
		print 'error', e
	finally:
		print 'finally'


main()


# logging

print '*****'
# throw
class FooError(ValueError):
	pass


def foo1(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value:%s' % s)
	return 10 / n
def bar1():
	try:
		foo1('0')
	except ValueError as e:
		print 'ValueError'
		raise ValueError('input error')

bar1()


