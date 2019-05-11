#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
character	ASCII	Unicode[PAM]		UTF-8[transform]
A	01000001	00000000 01000001	01000001
中	x	01001110 00101101	11100100 10111000 10101101
'''

print ('包含中文的str')

# ord() a character
print ord('A')
# print ord('中') three


# chr() range(256)
print chr(66)
# print chr(25991)

# ascii-unicode-[utf8]
x = 'ABC'
y = b'ABC'
z0 = '中文'
z1 = '\xe4\xb8\xad\xff'

#  str-->bytes
print x.encode('ascii')
print y.encode('ascii')
print y.encode('utf-8')
print len(x)
print len(y)
print len(z0)
print len(z1)

#  bytes-->str
print y.decode('ascii')
print z0.decode('utf-8')  # bytes
print z1.decode('utf-8', errors='ignore')
print len(z0.decode('utf-8'))
