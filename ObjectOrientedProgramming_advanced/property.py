#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         property
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

class Student(object):
	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100')
		self._score = value

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2019 - self._birth


s = Student()
s.set_score(90)
print s.get_score()

# s.set_score(101)
# print s.get_score()
