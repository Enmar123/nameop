# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:32:56 2019

@author: Jason
"""

from nameop import nameop as op

file = op('/home/arc/files/myfile.txt')

file.add_op('kek')

print(file.dir)
print(file.name)
print(file.ext)

print(file)

