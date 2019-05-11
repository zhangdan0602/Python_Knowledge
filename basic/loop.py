#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         loop
# Description:  
# Author:       Zd
# Date:         2019/5/11
# -------------------------------------------------------------------------------

# for
classmates = ['mike', 'amy', 'lily']
for name in classmates:
	print name

sum = 0
for x in [1, 2, 3, 4, 5]:
	sum = sum + x
print sum

sum = 0
for x in range(101):
	sum = sum + x
print sum

l = list(range(101))
sum = 0
for x in l:
	sum = sum + x
print sum

# while
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print sum

# break
n = 1
while n < 5:
	print n
	n = n + 1
print 'end'

n = 1
while n < 10:
	if n > 5:
		break;
	print n
	n = n + 1
print 'end'

n = 1
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print n
print 'end'
