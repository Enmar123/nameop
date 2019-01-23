# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:32:56 2019

@author: Jason
"""

from nameop import filename

file = filename('/home/user/files/myfile_colored.txt')

print('')
print('--- Before Modification ---')
print(file)
print('')
print(file.name)
print(file.path)

file.add_op('FFT')
file.add_op('multiplied')
file.add_post('display')
file.add_op('RGBsubtracted')

print('')
print('--- After Modification 1 ---')
print(file)
print('')
print(file.name)
print(file.path)

file.add_pre('001')
file.add_dir('filetypeA')
file.rep_sep('-')

print('')
print('--- After Modification 2 ---')
print(file)
print('')
print(file.name)
print(file.path)
print('')
print('OriginalFile =', file.original)