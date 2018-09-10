#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:09:44 2018

@author: raunak
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 18:50:45 2018

@author: raunak
"""
balance = 320000
annualInterestRate = 0.2
lowbound=balance/12
upbound =(balance * (1 + (annualInterestRate/12))**12) / 12.0 
epilson=0.02
while abs(balance)>epilson:
    '''
      # payment:monthly minimum payment
      #balance:debt balance
      returns balance at the end of 1 year
    '''
    payment = (lowbound+upbound)/2
    month = 0 #loop varialble
    #loop to calculate each months remaining balance
    while month < 12:
        remain = balance - payment  #remaining balance in current month
        balance = round(remain*(annualInterestRate)/12,2)+remain
        #to make sure valculation is going right 
        #print monthly debt
        #print(" Remaining balance: ",round(balance,2))
        month+=1
    if balance > epilson:
        print(payment)
        lowbound=payment
    elif balance < -epilson:
        upbound=payment
    else:
        break

print("Lowest Payment: ",payment)