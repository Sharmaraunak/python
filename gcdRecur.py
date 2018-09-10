#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:59:26 2018

@author: raunak
"""

def gcdRecur(a,b):
    '''
    a,b:positive integers
    returns greatest common divisor
    '''
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)