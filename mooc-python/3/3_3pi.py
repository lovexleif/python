# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:37:50 2017

@author: xie
"""

#PI jisuan
#pi.py
import random
import math
import time

DARTs = 1200
hits = 0
time.clock()
for i in range(1, DARTs):
    x, y = random.random(), random.random()
    dist = math.sqrt(x**2 + y**2)
    if dist < 1.0:
        hits = hits + 1
pi = 4 * hits/DARTs
print('Pi value is :{}'.format(pi))
print('this programer starts :{0:.2f}s'.format(time.clock()))