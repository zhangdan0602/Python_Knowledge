#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         debug
# Description:  
# Author:       Zd
# Date:         2019/5/15
# -------------------------------------------------------------------------------
import pdb

import logging

logging.basicConfig(level=logging.INFO)


# print

# assert
def foo(s):
	n = int(s)
	# -o
	assert n != 0, 'n is zero'
	return 10 / n


def main():
	foo('1')


main()


# logging
def log(s):
	s = '1'
	n = int(s)
	logging.info('n=%d' % n)
	print 10 / n


# pdb
# python -m pdb debug.py

def pdb0(s):
	s = '0'
	n = int(s)
	pdb.set_trace()
	print 10 / n


pdb0('0')

# ide
