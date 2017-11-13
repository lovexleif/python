#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:52:19 2017

@author: xie
"""
from turtle import Turtle

p = Turtle()
p.speed(1)
p.pensize(5)
p.color('black', 'yellow')
p.begin_fill()
for i in range(5):
    p.forward(200)
    p.right(144)
p.end_fill()