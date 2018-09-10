#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:21:38 2018

@author: raunak
"""

def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  
