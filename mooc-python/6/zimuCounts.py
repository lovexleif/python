#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 18:27:59 2017

@author: xie
"""
# tongji zimu
# can use seach.txt or seach2.txt
import turtle
## quanju bianliang##
# wordCounts number
count = 10
# word frequent y
data = []
# word x
words = []
# y fangda beis
yScale = 0.32
# x fangda beis
xScale = 30

############# TURTLE START###########
def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


def drawText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.write(text)


def drawRectangle(t, x, y):
    x = x*xScale
    y = y*yScale
    drawLine(t, x-5, 0, x-5, y)
    drawLine(t, x-5, y, x+5, y)
    drawLine(t, x+5, y, x+5, 0)
    drawLine(t, x+5, 0, x-5, 0)


def drawBar(t):
    for i in range(count):
        drawRectangle(t, i+1, data[i])


def drawGraph(t):
    drawLine(t, 0, 0, 360, 0)
    drawLine(t, 0, 0, 0, 300)
    for x in range(count):
        x = x + 1
        drawText(t, x*xScale-4, -20, (words[x-1]))
        drawText(t, x*xScale-4, data[x-1]*yScale+10, data[x-1])
    drawBar(t)
###############TURTLE END  ###################


def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*123456789-_—\n-()_+-=-<>?/,.:;[]{}|\!''""":
            line = line.replace(ch, '')
    return line


def processline(line, wordCounts):
    line = replacePunctuations(line)
    words = [ch for ch in line]
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


def main():
    fileName = input('input a file name:').strip()
    infile = open(fileName, 'r')
    
    wordCounts = {}
    for line in infile:
        processline(line.lower(), wordCounts)
    
    pairs = list(wordCounts.items())
    items = [[x, y] for (y, x) in pairs]
    items.sort()
    for i in range(len(items)):
        if items[i][1] == ' ':
            items.pop(i)
    for i in range(len(items)-1, len(items)-count-1, -1):
        print(items[i][1]+'\t'+str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
    infile.close()
    
    turtle.title('wordCounts chart')
    turtle.setup(900, 750, 0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    
    drawGraph(t)


if __name__ == '__main__':
    main()