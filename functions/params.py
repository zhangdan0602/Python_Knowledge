#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         params
# Description:  
# Author:       Zd
# Date:         2019/5/12
# -------------------------------------------------------------------------------

# location params
def power2(x):
	return x * x


def powern(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


print power2(5)
print powern(5, 3)


# default params[no modify]

def powern2(x, n=3):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


print powern2(5)


def enroll(name, gender, age=6, city='beijing'):
	print 'name %s' % name
	print 'gender %s' % gender
	print 'age %s' % age
	print 'city %s' % city


enroll('ne', 'f')
enroll('nm', 'm', 7)
enroll('na', 'm', city='shanghai')


#  params is also variable
def add_end(l=[]):
	l.append('end')
	return l


print add_end([1, 2, 3])
print add_end(['x', 'y'])


def add_end_no_modify(l=None):
	if l is None:
		l = []
	l.append('end')
	return l


print add_end_no_modify()
print add_end_no_modify()


def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


print calc([1, 2, 3])


# modify params
def calc1(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum


print calc1(1, 2, 3)
nums = [1, 2, 3]
print calc1(*nums)


# key params
def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:', name, 'age:', age, 'other:', kw)


person('micle', 22)
person('bob', 23, city='beijing')
person('amy', 24, gender='f', city='beijing')

extra = {'gender': 'm', 'city': 'beijing', 'job': 'engineer'}
person('mike', 25, job=extra['job'])
person('jack', 26, **extra)


# name params
# def person1(name, age, *, city, job):[python3]
def person1(name, age, *city):
	print('name:', name, 'age:', age, 'city:', city)


person1('Jack', 24, 'Beijing')


def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

#def f2(a, b, c=0, *,d, **kw):
def f2(a, b, c=0, *d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, ('a', 'b'))
f1(1, 2, 3, ('a', 'b'), x=99)

f2(1, 2)
f2(1, 2, 3)
f2(1, 2, 3, ('a', 'b'))
f2(1, 2, 3, ('a', 'b'), x=99)
f2(1, 2, 3, 99, ext=None)
f2(1, 2, 3, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
#  python2:before 2;python3:each value
f1(args, kw)
f2(args, kw)
