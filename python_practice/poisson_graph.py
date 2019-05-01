# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:29:00 2017

@author: Inderpreet
"""

from matplotlib import pylab as pl
import math
pl.style.use('ggplot')
def poisson(n,mu):
    return(math.pow(mu,n)*math.exp(-1*mu)/math.factorial(n))

def plot(mu):
    x=[]
    y=[]
    for i in range(20):
        x.append(i)
        y.append(poisson(i,mu))
        print("n=",i," P(n)=",y[i])
        
    pl.plot(x,y)

mu=7
plot(mu)
pl.savefig("Poisson_Boas_ggplot.png")
pl.show()