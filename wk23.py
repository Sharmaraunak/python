#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 00:54:09 2018

@author: raunak
"""

iteration = 0
while iteration < 5:
    count =0
    for letter in "hello, world":
        count+=1
        if iteration %2 == 0:
            break
    print("Iteration "+str(iteration)+";count is: " + str(count))
    iteration+=1