#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:10:03 2017

@author: xie
"""
from turtle import *


def ReadData():
    result = []
    file = open('data.txt', 'r')
    for line in file:
        result.append(list(map(float, line.split(','))))
    print(result)
    file.close()
    return result


def DrawPath(result):
    title('数据驱动的动态路径绘制')
    setup(800, 600, 0, 0)
    width(5)
    shape('turtle')
    speed(10 )
    for i in range(len(result)):
        print(result[i][1])
        color((result[i][3], result[i][4], result[i][5]))
        fd(result[i][0])
        if result[i][1]:
            turtle.rt(result[i][2])
        else:
            lt(result[i][2])
    goto(0, 0)


def main():
    result = ReadData()
    DrawPath(result)


if __name__ == '__main__':
    main()
