#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:36:46 2018

@author: raunak
"""
from math import *

def polysum(n,s):
    '''
    input:n,number of sides;s,side-length
    returns sum of the AREA and square of perimeter of regular 
    polygon
    '''
    perimeter = n*s
    square = ((0.25*n*(s**2))/tan(pi/n))
    
    return round(square,4)+(perimeter**2)