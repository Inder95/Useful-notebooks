# -*- coding: utf-8 -*-
"""
Created on Sat May 20 09:04:25 2017

@author: Inderpreet
"""

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


def z_const(fig):    
    r=np.arange(0,1,0.1)
    theta = np.linspace(0,2*math.pi,100, endpoint=False)
    
    X= []
    Y= []
    for i in r:
        for j in theta:
            X.append(i*math.cos(j))
            Y.append(i*math.sin(j))        
    
    Z = np.full(len(X),2)
    
    graph1 = fig.add_subplot(1,3,1, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.rainbow))


def r_const(fig):    
    z=np.arange(0,1,0.01)
    theta = np.linspace(0,2*math.pi,len(z), endpoint=False)
    r = 1
    X=[]
    Y=[]
    Z=[]
    for i in theta:
        for j in z:
            X.append(r*math.cos(i))
            Y.append(r*math.sin(i))
            Z.append(j)
        
#        
    
    graph1 = fig.add_subplot(1,3,2, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.cool))

def theta_const(fig):    
    z=np.arange(0,1,0.01)
    r=np.arange(0,1,0.01)
    theta = math.pi/4.0
    
    X=[]
    Y=[]
    Z=[]
    for i in r:
        for j in z:
            X.append(i*math.cos(theta))
            Y.append(i*math.sin(theta))
            Z.append(j)
    
    graph1 = fig.add_subplot(1,3,3, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.coolwarm))

def main():
    fig = plt.figure()
    z_const(fig)
    r_const(fig)
    theta_const(fig)
    plt.savefig("Cylindrical Co-ordinate surfaces.jpg")

if __name__=="__main__":
    main()