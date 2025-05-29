# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:35:31 2024

@author: Labide
"""

import scipy.stats as sts
import numpy as np
from matplotlib import pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)
uniform_dist = sts.uniform.pdf(mu) + 1


def likelihood_func (datum, mu):
  likelihood_out = sts.norm.pdf(datum, mu, scale = 0.1) 
  return likelihood_out/likelihood_out.sum()

likelihood_out = likelihood_func(1.7, mu)

plt.plot(mu, likelihood_out)
plt.title('Likelihood of $\mu$ given observation 1.7')
plt.ylabel('Probability of Density')
plt.xlabel('Value of $\mu$')
plt.show()