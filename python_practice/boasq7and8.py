# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from matplotlib import pylab as pl
import math
p=4/5
def ncx(n,x):
    return(math.factorial(n)*math.pow(p,x)*math.pow((1-p),(n-x))/(math.factorial(n-x)*math.factorial(x)))

def density_function_graph(n):
    y=[]
    x=[]
    for i in range(n+1):
        x.append(i)
        y.append(ncx(n,i))
    fig.add_subplot(311)
    pl.title("Probability Density")
    pl.plot(x,y)

def cumulative_density_function_graph(n):
    y=[]
    x=[]
    for i in range(n+1):
        x.append(i)
        y.append(sum([ncx(n,j) for j in range(i+1)]))
    print("x=",x)
    print("y=",y)
    fig.add_subplot(312)
    pl.title("Cumulative Probability")
    pl.plot(x,y)

def plot_nfx(n):
    y=[]
    x=[]
    for i in range(n+1):
        x.append(i/n)
        y.append(n*ncx(n,i))
    fig.add_subplot(313)
    pl.title("n f(x)  vs. x/n")
    pl.plot(x,y)
    

n=[50]
fig=pl.figure()
for i in n:
    cumulative_density_function_graph(i)
    density_function_graph(i)
    plot_nfx(i)
pl.savefig("boas_q8.jpg")
pl.show()           
    