#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         unit_test
# Description:  
# Author:       Zd
# Date:         2019/5/15
# -------------------------------------------------------------------------------
import unittest
from mydict import Dict

d = dict(a=1, b=2)
print d['a']


class TestDict(unittest.TestCase):
	def setUp(self):
		print 'setUp..'

	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	def tearDown(self):
		print 'tearDown..'


if __name__ == '__main__':
	unittest.main()

# python -m unittest .py
