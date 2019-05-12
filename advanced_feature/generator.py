#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         genertor
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------

# list
l = [x * x for x in range(1, 11)]
print l

# generator
g = (x * x for x in range(1, 11))
print g
print next(g)
for n in g:
	print n


# fib
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	# return 'Done'

for i in fib(10):
	print i

g = fib(6)
while True:
	try:
		x = next(g)
		print x
	except StopIteration as e:
		print e.value
		break
