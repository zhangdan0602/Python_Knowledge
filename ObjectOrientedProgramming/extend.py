#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         extend
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

# extend and polymorphic
class Animal(object):
	def run(self):
		print 'Animal is running..'


class Dog(Animal):
	def run(self):
		print 'dog is running..'

	pass


class Cat(Animal):
	def run(self):
		print 'cat is running..'

	pass


class Timer(object):
	def run(self):
		print 'start'


def run_twice(animal):
	animal.run()
	animal.run()


dog = Dog()
dog.run()

cat = Cat()
cat.run()

l = list()
a = Animal()

print isinstance(l, list)
print isinstance(a, Animal)
print isinstance(cat, Cat)
print isinstance(dog, Animal)

run_twice(Animal())
run_twice(Dog())
run_twice(Timer())


# static language
#  Animal/son
# dynamic language
#  run()
