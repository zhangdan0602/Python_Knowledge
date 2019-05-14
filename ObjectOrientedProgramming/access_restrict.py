#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         access_restrict
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

class Student(object):
	# intern
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	# encapsulation data
	def print_score(self):
		print '%s %s' % (self.__name, self.__score)

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')


bart = Student('Bart Impson', 59)
print bart
print Student
bart.print_score()
print bart.get_grade()
print bart.get_name()
print bart._Student__name

