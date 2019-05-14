#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         getObjectInformation
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

import types


class Animal(object):
	def run(self):
		print 'Animal is running..'


class Dog(Animal):
	def run(self):
		print 'dog is running..'

	pass


a = Animal()
dog = Dog()

# type
print type(123)
print type('str')
print type(None)

print type(abs)
print type(a)

print type(123) == type(456)
print type('abc') == type(123)

print type(lambda x: x) == types.LambdaType

# instance
print isinstance(dog, Dog)
print isinstance(dog, Animal)
print isinstance([1, 3, 4], (list, tuple))

# dir()
print dir('str')
print len('123')
print '123'.__len__()
print 'ABCFD'.lower()


class MyObject(object):
	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x


# attr
obj = MyObject()
print hasattr(obj, 'x')
print hasattr(obj, 'y')
print setattr(obj, 'y', 20)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y

# method
print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn
print fn()
