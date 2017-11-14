#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:53:15 2017

@author: xie
"""


def ReadData():
    ftele1 = open('TeleAddressBook.txt', 'rb')
    ftele2 = open('EmaiAddressBook.txt', 'rb')
    ftele1.readline()
    ftele2.readline()
    line1 = ftele1.readlines()
    line2 = ftele2.readlines()
    return line1, line2


def GetElements(line1, line2):
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_email = []
    for line in line1:
        elements = line.split()
        list1_name.append(str(elements[0].decode('utf-8')))
        list1_tele.append(str(elements[1].decode('utf-8')))
    for line in line2:
        elements = line.split()
        list2_name.append(str(elements[0].decode('utf-8')))
        list2_email.append(str(elements[1].decode('utf-8')))
    lines = []
    lines.append('姓名\t电话\t邮箱\n')
    for i in range(len(list1_name)):
        s = ''
        if list1_name[i] in list2_name:
            j = list2_name.index(list1_name[i])
            s = '\t'.join((list1_name[i], list1_tele[i], list2_email[j]))
            s += '\n'
        else:
            s = '\t'.join((list1_name[i], list1_tele[i], str(' ----- ')))
            s += '\n'
        lines.append(s)
    for i in range(len(list2_name)):
        s = ''
        if list2_name[i] not in list1_name:
            s = '\t'.join((list2_name[i], str(' ----- '), list2_email[i]))
            s += '\n'
        lines.append(s)
    return lines


def WriteFile(lines):
    ftele3 = open('AddressBook.txt', 'w')
    ftele3.writelines(lines)


def main():
    line1, line2 = ReadData()
    lines = GetElements(line1, line2)
    WriteFile(lines)
    print(' bingo ! This program runs')


if __name__ == '__main__':
    main()
