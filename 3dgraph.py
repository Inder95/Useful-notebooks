# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:32:03 2017

@author: Inderpreet
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math

x=np.arange(0,10,0.1)
y=np.arange(0,30,0.1)
X,Y =np.meshgrid(x,y)

sum=0
for i in range (1,20):
    sum=sum+(-1)**(i+1)*np.exp(-0.1*i*np.pi*Y)*np.sin(0.1*np.pi*X*i)
sum=sum*20/np.pi
Z=sum

graph= Axes3D(plt.figure())

surf= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)

plt.savefig("3D Graph.jpg")