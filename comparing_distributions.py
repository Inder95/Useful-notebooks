# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 03:17:00 2017

@author: Inderpreet
"""

from matplotlib import pylab as pl
import math
from decimal import *
getcontext().prec=6


#Binomial
def ncx(n,x,p):
    return((Decimal(math.factorial(n))*Decimal(math.pow(p,x))*Decimal(math.pow((1-p),(n-x)))/(Decimal(math.factorial(n-x))*Decimal(math.factorial(x)))))

def density_function_graph(n,p):
    y=[]
    x=[]
    for i in range(n+1):
        x.append(i)
        y.append(ncx(n,i,p))
    
    pl.title("Probability Density")
    pl.plot(x,y,label='Binomial')

#Gaussian
def probability_function(x,mu,sigma):
    return (math.exp(-1*math.pow(x-mu,2)/(2*math.pow(sigma,2)))/(sigma*math.pow(2*math.pi,0.5)))


def plot_gaussian(mu,sigma):
    x=[]
    y=[]
    for i in range(0,1500,1):
        x.append(i)
        y.append(probability_function(i,mu,sigma))
           
    pl.plot(x,y,label='Gaussian')

#Poisson
def poisson(n,mu):
    return(math.pow(mu,n)*math.exp(-1*mu)/math.factorial(n))

def plot_poisson(mu):
    x=[]
    y=[]
    for i in range(20):
        x.append(i)
        y.append(poisson(i,mu))
        print("n=",i," P(n)=",y[i])
    pl.plot(x,y,label='Poisson')
        
n=1500
p= (1/500)
pl.xlim(0,20)
density_function_graph(n,p)
plot_gaussian(n*p,math.sqrt(n*p*(1-p)))
plot_poisson(n*p)
pl.legend()
pl.savefig("comparison.pdf")
pl.show()