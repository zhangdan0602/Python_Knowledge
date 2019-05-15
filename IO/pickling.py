#! /usr/bin/python
# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         pickling
# Description:  
# Author:       Zd
# Date:         2019/5/15
# -------------------------------------------------------------------------------

# pickle
import pickle
import json

d = dict(name='bob', age=20)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
print 'python-----file'
print pickle.dumps(d)

print 'python-----json'
print json.dumps(d)

print 'json-----python'
json_str='{"age": 20, "name": "bob"}'
print json.loads(json_str)


# unpickle
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print 'file-----python'
print d


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('bob',20,88)

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print 'class-----json'
print json.dumps(s,default=student2dict)
print json.dumps(s,default=lambda obj:obj.__dict__)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str='{"age": 20, "name": "bob","score":88}'
print 'json-----class'
print json.loads(json_str,object_hook=dict2student)


