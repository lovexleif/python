#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:31:30 2017

@author: xie
"""
#n!
def fact(n) :
    if n ==0:
        return 1
    else:
        return n*fact(n-1)
# reverse
def reverse(s):
    if s == '':
        return s
    else:
        print(s)
        return reverse(s[1:])+s[0]