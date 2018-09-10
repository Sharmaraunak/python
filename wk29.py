#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 01:09:16 2018

@author: raunak
"""

x=float(input("enter a decimal number between 0 and 1: "))

p = 0
while (x*(2**p))%1!=0:
    p+=1
num = int(x*(2**p))
if num == 0:
    print("binary : 0")
else:
    binary = ''
    while num > 0:
        rem = num%2
        binary = str(binary) + str(rem)
        num=num//2
    for i in range(p-len(binary)):
        binary = '0'+ binary
    binary = binary[0:-p]+"."+binary[-p:]
    print("binary of ",str(x)+": "+binary)