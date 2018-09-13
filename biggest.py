#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:21:05 2018

@author: raunak
"""

def biggest(aDict):
    numvalue = {}
    for e in aDict:
        numvalue[e] = len(aDict[e])
    return numvalue