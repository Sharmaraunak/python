#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:28:35 2018

@author: raunak
"""

low=0
high = 100
guess = int((low+high)/2)
print("Please think of a number between 0 and 100!")
print("Is your secret number ",str(guess),"?")

while low < high:
    s=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if s == 'l':
        low=guess
        guess = int((guess+high)/2)
        print("Is your secret number ",str(guess),"?")
    elif s == 'h':
        high = guess
        guess=int((low+guess)/2)
        print("Is your secret number ",str(guess),"?")
    elif s == 'c':
        print("Game over.your secret number was:",str(guess))
        break
    else:
        print("Game over.your secret number was:",str(guess))
        print("Sorry, I did not understand your input")
        
        
        