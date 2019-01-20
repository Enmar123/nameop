# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:32:56 2019

@author: Jason
"""

from nameop import filename

file = filename('/home/arc/files/myfile.txt')

print('')
print('--- Before Modification ---')
print(file)
print('')
print(file.dir)
print(file.pre_op)
print(file.desc)
print(file.op)
print(file.post_op)
print(file.ext)

file.add_op('kek')
file.add_op('mult')
file.add_post('display')
file.add_op('subtract')

print('')
print('--- After Modification ---')
print(file)
print('')
print(file.dir)
print(file.pre_op)
print(file.desc)
print(file.op)
print(file.post_op)
print(file.ext)

print('')
print(file.name)
print(file.path)

