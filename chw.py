#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:54:32 2018

@author: raunak
"""

init_balance = 3200000
monthlyInterestRate = 0.2/12
lower = init_balance/12
upper = (init_balance * (1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
        print(balance)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))
