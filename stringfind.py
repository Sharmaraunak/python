#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:34:11 2018

@author: raunak
"""

def isIn(char,aStr):
    l=len(aStr)
    if l <= 1:
        if char!=aStr:
            return False
        else:
            return True
    else:
        mid=int((0+l)/2)
        if char < aStr[mid]:
            return isIn(char,aStr[0:mid])
        elif char > aStr[mid]:
            return isIn(char,aStr[mid:l])
        elif char == aStr[mid]:
            return True