# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:33:29 2023

"""
#One way to find out the last digit of a number is to mod the number by 10 
#Write a program that asks the user to enter power 
#Then find the last digit of 2 raised to that power
import math
power = int(input("Enter power: "))
sq = 2**power
print(sq % 10)
