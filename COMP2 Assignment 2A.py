# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:59:28 2023

"""
# Write a program that generates a 5 random decimal number between 1 and 100
# with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00 
# Compute the average of the numbers.
import random
num1 = (round(random.uniform(1, 100), 2))
num2 = (round(random.uniform(1, 100), 2))
num3 = (round(random.uniform(1, 100), 2))
num4 = (round(random.uniform(1, 100), 2))
num5 = (round(random.uniform(1, 100), 2))
print("num1:", num1, "\n","num2:", num2,"\n", "num3:", num3, "\n", "num4:", num4, "\n", "num5:", num5, sep="")
print("sum =", num1+num2+num3+num4+num5)