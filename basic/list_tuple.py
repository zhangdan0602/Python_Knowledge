#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         list_tuple
# Description:  
# Author:       Zd
# Date:         2019/5/11
# -------------------------------------------------------------------------------

# list[modify]
classmates = ['mike', 'amy', 'lily']
print classmates
print classmates[0]
print len(classmates)
print classmates[-1]

classmates.append('micle')
print classmates

classmates.insert(1, 'jordan')
print classmates

classmates.pop()
print classmates

classmates.pop(1)
print classmates

classmates[1] = 'sarah'
print classmates

l0 = ['nlp', 'cv']
l0.sort()
print l0
l = ['Apple', 123, True, 1.23, ['java', 'c'], l0]
print len(l)
print l[4][1]
print l[5][0]

# tuple[no modify except including list]
t = (1,)
print t
courses = ('chinese', 'math', 'english', ['java', 'c'])
print courses
