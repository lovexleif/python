#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 09:28:13 2017

@author: xie
"""

def main():
    try:
        sum = 0.0
        count = 0
        xstr = input('please input a number>>')
        while xstr != '':
            sum = sum + eval(xstr)
            count = count + 1
            xstr = input('please input a number>>')
        print('the average is {0:.2f}'.format(sum/count))
    except:
        print('shu ru cuo wu')
    else:
         print('bingo')
main()
