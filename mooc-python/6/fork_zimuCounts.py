#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 00:25:23 2017

@author: xie
"""

#显示个数

count = 10

#字母频率数组

data = []

#字母数组

words = []

#对文本的每一行计算字母频率的函数

def processLine(line, wordCounts):

    #删除包括空格的所有标点符号

    line = replacePunctuations(line)

    #从每一行获取每个字母

    for word in line:

        if word in wordCounts:

            wordCounts[word] += 1

        else:

            wordCounts[word] = 1

  

#删除标点的函数

def replacePunctuations(line):

    for ch in line:

        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""\ ":#增加空格

            line = line.replace(ch,"")

    return line

  

def main():

    #用户输入一个文件名

    filename = input("Enter a filename:").strip()

    infile = open(filename, "r")

      

    #建立用于计算字母的空字典

    wordCounts = {}

    for line in infile:

        processLine(line.lower(), wordCounts)

          

    #从字典中获取数据对

    pairs = list(wordCounts.items())

  

    #列表中的数据对交换位置,数据对排序

    items = [[x,y]for (y,x)in pairs] 

    items.sort() 

  

    #输出count个数词频结果

    for i in range(len(items)-1, len(items)-count-1, -1):

        print(items[i][1]+"\t"+str(items[i][0]))

        data.append(items[i][0])

        words.append(items[i][1])

          

    infile.close()

     

#调用main()函数

if __name__ == '__main__':

    main()

