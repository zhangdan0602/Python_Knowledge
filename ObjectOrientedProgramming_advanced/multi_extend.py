#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         multi_EXTEND
# Description:  
# Author:       Zd
# Date:         2019/5/14
# -------------------------------------------------------------------------------

class Animal(object):
	pass


class Mammal(Animal):
	pass


class Bird(Animal):
	pass


'''
class Dog(Mammal):
	pass
class Bat(Mammal):
	pass


class Parrot(Bird):
	pass
class Ostrich(Bird):
	pass

'''


class Runnable(object):
	def run(self):
		print 'run'


class Flyable(object):
	def fly(self):
		print 'fly'


# multiextend【mixIn】
class Dog(Mammal, Runnable):
	pass


class Bat(Mammal, Flyable):
	pass

# class MyTCPServer(TCPServer,ForkingMinIn):
# 	pass

# class MyUDPServer(UDPServer,ThreadingMinIn):
# 	pass

# class MyTCPServer(TCPServer,CoroutinMinIn):
# 	pass
