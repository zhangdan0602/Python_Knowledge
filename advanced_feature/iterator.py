#! /usr/bin/python
# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         iterator
# Description:  
# Author:       Zd
# Date:         2019/5/12
#-------------------------------------------------------------------------------

from collections import Iterable,Iterator
# iterable:for---list,set,dict,tuple,str,generator
# iterator:next()/iter()

# fib
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

g = fib(6)
print isinstance([],Iterable)
print isinstance((),Iterable)
print isinstance('',Iterable)
print isinstance({},Iterable)
print isinstance(g,Iterable)

print isinstance([],Iterator)
print isinstance((),Iterator)
print isinstance('',Iterator)
print isinstance({},Iterator)
print isinstance(g,Iterator)

print isinstance(iter([1,2]),Iterator)
print isinstance(iter((1,2)),Iterator)
print isinstance(iter('123'),Iterator)
print isinstance(iter({}),Iterator)
