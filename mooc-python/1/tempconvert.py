#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
  
#Tempconvert.py

val = input("请输入带温度表示符号的温度值（例如：32C）：")
if val[-1] in ['C','c']:
    f = 1.8 * eval(val[0:-1]) + 32
    print('转换后的温度为：%.2f F'%f)
elif val[-1] in ['F','f']:
    c = (eval(val[0:-1]) - 32) /18
    print('转换后的温度为：%.2f C'%c)
else:
    print('输入有误')
    

