#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 20:06:10 2017

@author: xie
"""
import turtle

# shezhi chuangkou xinxi
turtle.title('数据驱动的动态路径绘制')
turtle.setup(800, 600, 0, 0)
# she zhi huabi
pen = turtle.Turtle()
pen.color('red')
pen.width(5)
pen.shape('turtle')
pen.speed(1)

# duqu wenjian
result = []
file = open('data.txt', 'r')
for line in file:
    result.append(list(map(float, line.split(','))))
print(result)
file.close()
# dong tai huizhi
for i in range(len(result)):
    print(result[i])
    pen.color((result[i][3], result[i][4], result[i][5]))
    pen.fd(result[i][0])
    if result[i][1]:
        pen.rt(result[i][2])
    else:
        pen.lt(result[i][2])
pen.goto(0, 0)
