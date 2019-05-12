#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         slice
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------


# list
l = ['mike', 'sarah', 'bob', 'jack']
r = []
n = 3
for i in range(n):
	r.append(l[i])

print r

print l[0:3]
print l[:3]
print l[1:3]
print l[-1]
print l[-2:]
print l[-2:-1]

L = list(range(100))
print L
print L[:10]
print L[-10:]
print L[10:20]
print L[:10:2]
print L[::5]
print L[::]

# tuple
print (0, 1, 2, 3, 4)[:3]
print (0, 1, 2, 3, 4, 5, 6)[::2]
