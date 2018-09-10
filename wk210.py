#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 01:50:17 2018

@author: raunak
"""

epilson = 0.01
x = float(input("enter a number: "))
guess = x/2
numguess = 0
while abs(guess*guess- x)>=epilson:
    numguess+=1
    guess= guess-(((guess**2)-x)/(2*guess))
print("numguess = ",str(numguess))
print("root: ",str(guess))