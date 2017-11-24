#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:17:28 2017

@author: xie
"""
# kehou xiti 1
file = open('test.txt', 'w')
file.writelines(["中国是个伟大的国家"])
file.close()

# wenjian duru


def wenjian():
    file1 = open('test.txt', "r")
    print('wenjian duru:\n')
    for line in file1:
        print(line)
    file1.close()
# erjingz duru


def erjingz():
    file2 = open("test.txt", "rb")
    print('wenjian duru:\n')
    for line in file2:
        print(str(line.decode("utf-8")))
    file2.close()
