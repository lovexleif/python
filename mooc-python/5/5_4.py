#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:04:17 2017

@author: xie
"""

#shu
from turtle import Turtle

def tree(plist, l , a, f):
    '''
    plist is list of pens
    l is length of branch
    a is half of the angle between 2 branch
    f is factor by which branch is shortened
    '''
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)
            
    
def main():
    p = Turtle()
    p.color('black')
    p.pensize(5)
    p.hideturtle()
    #p.getscreen().tracer(1,0)
    p.speed(5)
    p.left(90)
    
    p.penup()
    p.goto(0, -200)
    p.pendown()
    
    tree([p], 200, 65, 0.6375)
main()
    