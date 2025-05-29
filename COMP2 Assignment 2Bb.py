# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:13:19 2023

"""
#One way to find out the last two digits of a number is to mod the number by 100
#Write a program that asks the user to enter power
#Then find the last two digits of 2 raised to that power
import math
power = int(input("Enter power: "))
sq = 2**power
print(sq % 100)