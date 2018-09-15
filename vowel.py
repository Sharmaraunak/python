#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 02:03:15 2018

@author: raunak
"""

s=input("Enter a word: ")
count = 0
for letter in s:
    if letter in ['a','e','i','o','u']:
        count +=1
print("Number of vowels:",count)