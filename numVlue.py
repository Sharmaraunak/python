#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:07:04 2018

@author: raunak
"""

def howMany(aDict):
    numValue =0
    for e in aDict:
        numValue = numValue+len(aDict[e])
    return numValue
        
        
    