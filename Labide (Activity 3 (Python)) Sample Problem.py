# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 23:09:41 2024

"""

#calculate probability of cancer patient and diagnostic test
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    #P(not A) formula
    not_a = 1 - p_a
    #P(B) formula
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    # P(A|B) formula
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

#Given
p_a = 0.0002
p_b_given_a = 0.85
p_b_given_not_a = 0.05
#Calc
result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)

print('P(A|B) = %.3f%%' % (result * 100))