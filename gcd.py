#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:47:17 2018

@author: raunak
"""

def gcdIter(a,b):
    '''
    input:a,b int>0
    returns gcd
    '''
    if a>b:
        num=b
    else:
        num=a
    while num >0:
        if a==1:
            return 1
        else:
            if b%num == 0 and a%num == 0:
                return num
            num-=1
            