#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         doc_test
# Description:  
# Author:       Zd
# Date:         2019/5/15
# -------------------------------------------------------------------------------


def abs(n):
	'''
	Function to get absolute value of number.

	Example:

	>>> abs(1)
	1
	>>> abs(-1)
	1
	>>> abs(0)
	0
	'''
	return n if n >= 0 else (-n)
