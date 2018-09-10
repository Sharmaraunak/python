#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:39:06 2018

@author: raunak
"""

def func_a():
    print("Inside func_a")
def func_b(y):
    print("inside func_b")
    return y
def func_c(z):
    print("inside func_c")
    return z()
print(func_a())
print(5+func_b(2))
print(func_c(func_a)
