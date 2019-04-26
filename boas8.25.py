# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:29:05 2017

@author: Inderpreet
"""

from scipy.stats import norm as np

print(np.cdf(0.5))

print("Boundary for marks such that 10% students get A grade: Mu +", np.ppf(0.9),"*sigma")