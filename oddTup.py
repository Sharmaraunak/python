#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 01:01:18 2018

@author: raunak
"""

def oddTuples(aTup):
    oddTup = ()
    for odd in range(len(aTup)):
        if odd%2 ==0:
            oddTup = oddTup + (aTup[odd],)
                
    return oddTup