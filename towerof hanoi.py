#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:19:35 2018

@author: raunak
"""

def printmov(fr,to):
    print("move from pillar",fr,"to pillar",to)
def tower(n,fr,to,spare):
    if n==1:
        printmov(fr,to)
    else:
        tower(n-1,fr,spare,to)
        tower(1,fr,to,spare)
        tower(n-1,spare,to,fr)
        
        

print("follow the steps to solve tower of hanoi")
tower(4,"p1","p2","p3")