#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:37:50 2017

@author: xie
"""

#shu ru 1 - 12 out months
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
n = input('input 1 -12')
pos = (int(n) - 1)*3
monthAbbrev = months[pos:pos+3]
print('yue fen jian xie wei : {}'.format(monthAbbrev)+'.')