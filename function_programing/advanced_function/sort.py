#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         sort
# Description:  
# Author:       Zd
# Date:         2019/5/13
# -------------------------------------------------------------------------------

# sort
print sorted([36, -5, 23, -21])
print sorted([36, -5, 23, -21], key=abs)
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
