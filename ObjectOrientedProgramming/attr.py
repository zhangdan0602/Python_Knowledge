#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         attr
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------


# instance attr
class Student(object):
	classname = 'Student'

	def __init__(self, name):
		self.name = name


a = Student('bob')
print a.name

s = Student('call')
print s.classname
s.classname = 'new'
# instance
print s.classname
print Student.classname

del s.classname
# class
print s.classname
