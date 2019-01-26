# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:32:56 2019

@author: Jason
"""

from nameop import filename

file = filename('Documents/myfile.txt')

# --- Start Test modifications ---


file.add_op("kek")
file.pop_dir()
file.add_dir('/')

# --- END Test modifications ---


print(file.dir)
print(file.desc)
print(file.ext)
print('')
print(file.name)
print(file.path)

