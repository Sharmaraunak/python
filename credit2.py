#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 15:55:05 2018

@author: raunak
"""
balance = 3329
annualInterestRate = 0.2
payment = 10
def finder(payment,balance):
    '''
      # payment:monthly minimum payment
      #balance:debt balance
      returns balance at the end of 1 year
    '''
    b1=balance#recursively preserve balance
    month = 0 #loop varialble
    #loop to calculate each months remaining balance
    while month<12:
        remain = balance - payment  #remaining balance in current month
        balance = round(remain*(annualInterestRate)/12,2)+remain
        #to make sure valculation is going right 
        #print monthly debt
        #print(" Remaining balance: ",round(balance,2))
        month+=1
    if balance>0:
        return finder(payment+10,b1)
    else:
        return payment
x=finder(payment,balance)
print("Lowest Payment: ",x)



    

   
   
