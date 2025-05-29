# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:13:43 2023

"""
#Write a program that asks the user to enter power and how many digits they want
#Find the last that many digits of 2 raised to the power the user entered
import math
power = int(input("Enter power: "))
print("Enter how many last digits to display")
mod = int(input("(10 shows one last digit, add 0 at the end for 1 more digit):\n"))
sq = 2**power
print("Last digit(s): \n", sq % mod)