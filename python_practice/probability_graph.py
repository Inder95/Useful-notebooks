# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:34:32 2017

@author: Inderpreet
"""

from matplotlib import pylab as pl
from decimal import *   
import math
p=0.5
getcontext().prec=6
def ncx(n,x):
    return((Decimal(math.factorial(n))*Decimal(math.pow(p,x))*Decimal(math.pow((1-p),(n-x)))/(Decimal(math.factorial(n-x))*Decimal(math.factorial(x)))))

def density_function_graph(n):
    y=[]
    x=[]
    for i in range(int(n+1)):
        x.append(i)
        y.append(ncx(n,i))
    pl.plot(x,y,label='Binomial')
    
def probability_function(x,mu,sigma):
    return (math.exp(-1*math.pow(x-mu,2)/(2*math.pow(sigma,2)))/(sigma*math.pow(2*math.pi,0.5)))

def plot(n,mu,sigma):
    x=[]
    y=[]
    for i in range(0,1000,1):
        x.append(i)
        y.append(probability_function(i,mu,sigma))
            
    pl.plot(x,y,label='Gaussian')

n=1000.0
density_function_graph(n)
plot(n,n*p,math.sqrt(n*0.5*0.5))
pl.legend()
pl.savefig("boas8.9.pdf")
pl.show()