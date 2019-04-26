# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:13:51 2017

@author: preet
"""

import random
import matplotlib.pyplot as plt
import numpy as np

random.seed(a=0)
fig = plt.figure(figsize =(35,10) )
fig1= plt.subplot(1,3,1)
fig2= plt.subplot(1,3,2)
fig3= plt.subplot(1,3,3)
#Generate exponentially distributed random variable with arrival rate 7.2
a1k= []
for i in range(1000):
    a1k.append(random.expovariate(7.2))
fig1.hist(a1k)

#Generate Uniformaly distributed random variable between [0.75,1.17]
a2k= []
for i in range(1000):
    a2k.append(random.uniform(0.75,1.17))
fig2.hist(a2k)

#Inter_arrival times
ak = np.array(a1k) *np.array(a2k)
fig3.hist(ak)
fig3.set_title("Distribution of inter-arrival times")

fig.savefig("Distribution tests.jpg")