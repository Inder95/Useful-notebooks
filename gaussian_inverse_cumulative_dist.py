# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:51:36 2017
This program tries to predict the Z of a Cumulative Distribution Function
using Scipy.

@author: Inderpreet
"""

from scipy.stats import norm as nd
print (nd.ppf(0.95))
