#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 01:24:31 2018

@author: raunak
"""

x=23
epilson = 0.01
step = 0.1
guess = 0.0
 
while  abs(guess**2 - x) >= epilson:
    if guess <= x:
        guess+=step
    else:
        break
        
if abs(guess**2 - x) >= epilson:
    print("failed")
else:
    print("succeeded: "+str(guess))
