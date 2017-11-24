#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:35:52 2017

@author: xie
"""
# Hamlet.py


def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_+-=-<>?/,.:;[]{}|\\!\"\'":
            line = line.replace(ch, ' ')
    return line


def processline(line, counts):
    line = replacePunctuations(line)
    words = line.split()
    excludes = ["the", "and", "to", "of", "you", "i", "a", "my", "in", "is",
                   "it", "that", "not", "this", "this", "his", "with", "for",
                   "s", "me", "as", "what"]
    for word in words:
        if word in excludes:
            continue
        counts[word] = counts.get(word, 0) + 1


def main():
    count = 10
    counts = {}
    fo = open("hamlet.txt", "rb")
    for line in fo:
        processline(line.decode("utf-8").lower(), counts)
    pairs = list(counts.items())
    items = [[x, y] for (y, x) in pairs]
    items.sort()
    for i in range(len(items)-1, len(items)-count-1, -1):
        print(items[i][1]+'\t'+str(items[i][0]))
    fo.close()


if __name__ == "__main__":
    main()
