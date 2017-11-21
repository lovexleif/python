#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:29:32 2017

@author: xie
"""

# li yong zidian hebing tongxulu
ftele1 = open('TeleAddressBook.txt', 'rb')
ftele2 = open('EmaiAddressBook.txt', 'rb')
ftele1.readline()
ftele2.readline()
lines1 = ftele1.readlines()
lines2 = ftele2.readlines()

dic1 = {}
dic2 = {}

for line in lines1:
    elements = line.split()
    dic1[elements[0]] = str(elements[1].decode('gbk'))

for line in lines2:
    elements = line.split()
    dic2[elements[0]] = str(elements[1].decode('gbk'))


lines = []
lines.append('姓名\t      电话      \t邮箱\n')

for key in dic1:
    s = ''
    if key in dic2.keys():
        s = '\t'.join([str(key.decode('utf-8')), dic1[key], dic2[key]])
        s += '\n'
    else:
        s = '\t'.join([str(key.decode('utf-8')), dic1[key], str('  -----   ')])
        s += '\n'
    lines.append(s)

for key in dic2:
    s = ''
    if key not in dic1.keys():
        s = '\t'.join([str(key.decode('utf-8')), str('  -----   '), dic2[key]])
        s += '\n'
    lines.append(s)

ftele3 = open('ADDRESSBOOK.txt', 'w')
ftele3.writelines(lines)

ftele3.close()
ftele1.close()
ftele2.close()
