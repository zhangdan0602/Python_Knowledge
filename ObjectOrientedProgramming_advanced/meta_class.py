#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         meta_class
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

# type()
def fn(self, name='world'):
	print 'hello,%s' % name


Hello = type('Hello', (object,), dict(hello=fn))

print type(Hello)
h = Hello()
print type(h)
print h.hello()


# metaclass
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)


# class MyList(list, metaclass=ListMetaclass):
# 	pass
#
#
# L = MyList()
# L.add(1)
# print L
