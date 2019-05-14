#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         use_module
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

# as doc notes
' a test module'

__author__ = 'mike'
import sys


def test():
	args = sys.argv
	print args
	if len(args) == 1:
		# terminal:./module/use_module.py
		print '-----'
		print 'one param.'
	elif len(args) == 2:
		# terminal:./module/use_module.py zd
		print '*****'
		print 'two params,one of is %s' % args[1]
	else:
		print '#####'
		print 'too many params'


# scope
# public:__xxx__  xxx
print __doc__
print __author__


# private:_xxx  __xxx
def _private_1(name):
	return 'hello,%s' % name


def _private_2(name):
	return 'hi,%s' % name


def greeting(name):
	#abstract encapsulation
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)

print greeting('zxc')

if __name__ == '__main__':
	test()
	print greeting('zxcv')
