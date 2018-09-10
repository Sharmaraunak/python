#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:32:14 2018

@author: raunak
"""

def recurPower(base,exp):
    if exp == 0:
        return 1
    else:
        return base*recurPower(base,exp-1)