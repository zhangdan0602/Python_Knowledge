#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         condition
# Description:  
# Author:       Zd
# Date:         2019/5/11
# -------------------------------------------------------------------------------

# if
age = 16
if age > 18:
	print 'teenager'
elif age > 6:
	print 'adult'
else:
	print 'kid'

x = True
x = 1
x = 'str'
x = ['12']
if x:
	print 'True'

birth = input('birth:')
print type(birth)
if birth > 2000:
	print 'after 00'
else:
	print 'before 00'
