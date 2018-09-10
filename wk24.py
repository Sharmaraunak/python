#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 01:16:29 2018

@author: raunak
"""
x=25
epilson = 0.01
step = 0.1
guess = 0.0
numcount = 0
while guess <= x:
    numcount+=1
    if abs(guess**2 - x) < epilson:
        break
    else:
        guess+=step
        
if abs(guess**2 - x) >= epilson:
    print("failed")
else:
    print("succeeded: "+str(guess))
print(numcount)
