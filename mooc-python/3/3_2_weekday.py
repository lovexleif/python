# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:37:50 2017

@author: xie
"""

#shu ru 1 - 7 xing qi
weekday = 'MONTUEWEDTHUFRISATSUN'
n = input('input 1 -7')
pos = (int(n) - 1)*3
monthAbbrev = weekday[pos:pos+3]
print(': {}'.format(monthAbbrev)+'.')