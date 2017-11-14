#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:30:58 2017

@author: xie
"""
infile = open('1.txt', "r")
for i in range(5):
    line = infile.readline()
    print(line[:-1])