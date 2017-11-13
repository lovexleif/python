#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 20:24:06 2017

@author: xie
"""

def happy():
    print('Happy Birthday!')
def singPerson(person):
    happy()
    happy()
    print('Happy Birthday,dear',person+'!')
    happy()
def main():
    singPerson('Mike')
    print()
    singPerson('Lily')
main()
