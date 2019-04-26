# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:18:43 2017

@author: Inderpreet
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:07:10 2017

@author: Inderpreet
"""

from matplotlib import pylab as pl
import math

def probability_function(x,mu,sigma):
    return (math.exp(-1*math.pow(x-mu,2)/(2*math.pow(sigma,2)))/(sigma*math.pow(2*math.pi,0.5)))


def plot(mu,sigma):
    x=[]
    y=[]
    for i in range(-20,20,1):
        x.append(i)
        y.append(probability_function(i,mu,sigma))
    pl.xlim(-25,25)        
    pl.plot(x,y,label=sigma)
    
    
sigma=[1,2,5,1/6,1/3]
for i in sigma:
    plot(0,i)
pl.legend(loc='upper left',framealpha=0.25)
pl.savefig("boas6.jpg")
pl.show()
