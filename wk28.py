#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 23:08:04 2018

@author: raunak
"""
s = k= int(input("Enter a decimal number: "))
if s==0:
    print("Binary: 0")
else:
    binary=''
    while s > 0:
        rem = s%2
        binary = str(binary) + str(rem) 
        s=s//2
    print("Binary of "+str(k)+": ",str(binary))

    

        
