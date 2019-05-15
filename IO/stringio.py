#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         stringio
# Description:  
# Author:       Zd
# Date:         2019/5/15
# -------------------------------------------------------------------------------

from io import StringIO

# unicode
f = StringIO(u'123\n')
while True:
	s = f.readline()
	if s == '':
		break
	print s.strip()

# binary bytes
from io import BytesIO

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print f.read()

f.write('abc')
print f.getvalue()
