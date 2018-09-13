#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:38:21 2018

@author: raunak
"""

def square(a):
    return a*a

def halve(a):
    return a/2
 
def inc(a):
    return a+1

def applyToEach(L,x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
