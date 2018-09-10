#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 13:52:05 2018

@author: raunak
"""

x=25
epilson = 0.01
step = 0.1
guess = 0.0
numcount = 0
while guess <= x:
    numcount+=1
    guess+=step
print(numcount)