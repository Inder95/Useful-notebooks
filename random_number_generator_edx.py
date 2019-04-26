# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 09:51:46 2017

@author: Inderpreet
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np
def rng(seed, a, b, M, ntotal):
    data = np.zeros(ntotal)
    data[0] = seed
    for i in range(1,ntotal):
        data[i] = np.mod((a*data[i-1]+b), M)
    return data/np.float(M)

def auto_correlate(x):
    cor = np.correlate(x,x,mode="full")
    return cor[N-1:]

N=10**5
data = rng(123456,8121,28411,134456,N)
c = np.zeros(N)
c = auto_correlate(data-0.5)/N

plt.plot(c)
plt.xlim(-100,8000)
plt.xlabel(r'$i$',fontsize=16)
plt.ylabel(r'$\varphi(i)$',fontsize=16)
#print('\sigma^2 =',std**2)
plt.show()
