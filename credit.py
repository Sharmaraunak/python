#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:16:23 2018

@author: raunak
"""
#test case 1
balance = 484
annualIntrestRate = 0.2
monthlyPaymentRate = 0.04
month = 0 #loop varialble
#loop to calculate each months remaining balance
while month<12:
    payment = monthlyPaymentRate*balance #monthly minimum payment
    remain = balance - payment  #remaining balance in current month
    balance = round(remain*(annualIntrestRate)/12,2)+remain
    #to make sure valculation is going right 
    #print monthly debt
    #print(" Remaining balance: ",round(balance,2))
    month+=1
print(" Remaining balance: ",round(balance,2))    