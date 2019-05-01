# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 03:44:20 2017

@author: Inderpreet
"""



from matplotlib import pylab as pl
from decimal import *   
import math

#Gaussian
def probability_function(x,mu,sigma):
    return (math.exp(-1*math.pow(x-mu,2)/(2*math.pow(sigma,2)))/(sigma*math.pow(2*math.pi,0.5)))


def plot_gaussian(mu,sigma):
    x=[]
    y=[]
    for i in range(0,mu*3,1):
        x.append(i)
        y.append(probability_function(i,mu,sigma))
           
    pl.plot(x,y,label='Gaussian'+str(mu))

#Poisson
def poisson(n,mu):
    return(math.pow(mu,n)*math.exp(-1*mu)/math.factorial(n))

def plot_poisson(mu):
    x=[]
    y=[]
    for i in range(mu*3):
        x.append(i)
        y.append(poisson(i,mu))
    pl.plot(x,y,label='Poisson'+str(mu))

mu=[1,5,10,20,30]
fig=pl.figure()
pl.xlim(0,60)
for i in mu:
    plot_gaussian(i,math.sqrt(i))
    plot_poisson(i)
pl.legend()
pl.savefig("Poisson vs Gaussian.pdf")
pl.show()