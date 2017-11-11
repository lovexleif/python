#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 09:28:13 2017

@author: xie
"""
#BMI
def main():
    height = eval(input('Input your height(M):'))
    weight = eval(input('Input your weight(KG):'))
    BMI = weight/(height*height)
    print('Your BMI:{0:.2f}'.format(BMI))
    L = [0,0]
    leval = ['pianshou', 'zhengchang', 'pianpang', 'feipang']
    if BMI < 18.5:
        L[0], L[1] =leval[0],  leval[0]
    elif BMI >= 18.5 and BMI < 25:
        L[0] = leval[1]
    elif BMI >= 25 and BMI < 30:
        L[0] = leval[2]
    else:
        L[0] = leval[3]
    if BMI >= 18.5 and BMI < 24:
        L[1] = leval[1]
    elif BMI >= 24 and BMI < 28:
        L[1] = leval[2]
    elif BMI >= 28:
        L[1] = leval[3]
    print('guoji jian yi :{0}{2}guolei jian yi:{1}'.format(L[0],L[1],'\n'))
main()
