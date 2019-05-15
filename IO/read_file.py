#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         read_file
# Description:  
# Author:       Zd
# Date:         2019/5/15
# -------------------------------------------------------------------------------

# txt and utf8
# try
try:
	f = open('/Users/Zd/Desktop/Python_Knowledge/IO/read_file.py', 'r')
	# file-like Object
	print f.read()
finally:
	if f:
		f.close()

# =f.close()
with open('/Users/Zd/Desktop/Python_Knowledge/IO/read_file.py', 'r') as f:
	print f.read()

	for line in f.readlines():
		print line.strip()

# binary file
try:
	f = open('/Users/Zd/Desktop/Python_Knowledge/IO/read_file.py', 'rb')
	# file-like Object
	print f.read()
finally:
	if f:
		f.close()

# not utf8
try:
	f = open('/Users/Zd/Desktop/Python_Knowledge/IO/read_file.py', 'r', encoding='gbk', errors='ignore')
	# file-like Object
	print f.read()
finally:
	if f:
		f.close()

# write

try:
	f = open('/Users/Zd/Desktop/Python_Knowledge/IO/w.py', 'w')
	# file-like Object
	f.write('test')
finally:
	if f:
		f.close()

with open('', 'w')as f:
	f.write('hello')
