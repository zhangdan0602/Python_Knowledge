#! /usr/bin/python
# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         operate_fileordir
# Description:  
# Author:       Zd
# Date:         2019/5/15
#-------------------------------------------------------------------------------

# os
import os
print os.name
print os.uname()

# environ
print os.environ
print os.environ.get('PATH')

# file
print os.path.abspath('.')
print os.path.join('test')
# print os.mkdir('')
# print os.rmdir('')

print os.path.split('/Users/michael/testdir/file.txt')
print os.path.splitext('/Users/michael/testdir/file.txt')
# print os.rename('test.txt','test.py')
# print os.remove('test.py')

# shutil
print [x for x in os.listdir('../') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



