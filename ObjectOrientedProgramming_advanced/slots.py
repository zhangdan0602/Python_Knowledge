#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         slots
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

from types import MethodType


class Student(object):
	__slots__ = ('age', 'score', 'set_age')
	pass


s = Student()


# s.name = 'mike'
# print s.name


# instance
def set_age(self, age):
	self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print s.age


# class
def set_score(self, score):
	self.score = score


Student.set_score = set_score

s1 = Student()
s1.set_score(100)
print s1.score

s2 = Student()
s2.set_score(99)
print s2.score


class graduateStudent(Student):
	pass


g = graduateStudent()
g.name = 'g'
print g.name
