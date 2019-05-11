#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         format
# Description:  
# Author:       Zd
# Date:         2019/5/11
# -------------------------------------------------------------------------------

# %d, #f, %x, %s
print 'this str is %s' % 'world'
print 'these int number are %d-%02d' % (134, 4)
print 'this float number is %.2f' % 1.2345
print 'this hex number is %x' % 156
print 'not sure,use str %s' % True
print 'print rate: %d %%' % 7

# format
print '{0},{1:.1f}'.format('test', 3.1415)
