#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         Student
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

	# encapsulation data
	def print_score(self):
		print '%s %s' % (self.name, self.score)

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'


bart = Student('Bart Impson', 59)
print bart
print Student
bart.print_score()
print bart.get_grade()


# common
def print_score(std):
	print '%s %s' % (std.name, std.score)


print_score(bart)
