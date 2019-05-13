#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         decorator
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------
import functools


# variable = function
def now():
	print '2019'


d = now
print d()

print now.__name__
print d.__name__

print '-------------'


# decorator
def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)

	return wrapper


@log
def now1():
	print '2019-05'


rs = now1
print rs()

rs = log(now1)
print rs()


# receieve param
def log1(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print '%s %s()' % (text, func.__name__)
			return func(*args, **kw)

		return wrapper

	return decorator


@log1('execute')
def now2():
	print '2019-05-13'


print now2()

rs = log1('execute')(now2)
print rs()

print now2.__name__
print '-------------'


# functools
def log3(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s()' % func.__name__
		return func(*args, **kw)

	return wrapper


@log3
def now3():
	print 'now3-2019'


print now3()


def log4(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s()' % (text, func.__name__)
			return func(*args, **kw)

		return wrapper

	return decorator


@log4('execute')
def now4():
	print '2019-05-13'


print now4()
