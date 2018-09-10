#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:24:17 2018

@author: raunak
"""
##print("enter the base: ")
#base = eval(input())
#print("enter the exponential power: ")
#exp = int(input())
def iterPower(base,exp):
    result =1
    while exp > 0:
        result = result*base
        print(result)
        exp-=1
    return result



