#! /usr/bin/python
# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         dict
# Description:  
# Author:       Zd
# Date:         2019/5/11
#-------------------------------------------------------------------------------

# dict[no modify]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Bob']

d['Adam'] = 90
print d

print d.get('Thu')
print d.get('Thu',-1)

d.pop('Bob')
print d

d00 = (1,2,3)
d01 = {(1,2,3): 95}
print hash(d00)
d10 = (1,[2,3])

# set[no modity]
s = set([1, 2, 3,d00])
#s = set([1, 2, 3,d10])
print s
s.add(4)
print s
s.remove(4)
print 4
s1 = set([2,3,4,5])
print s & s1
print s | s1

# modify
l0 = ['nlp', 'cv']
l0.sort()
print l0

# no modify
str = '124'
str1 = str.replace('4','3')
print str
print str1