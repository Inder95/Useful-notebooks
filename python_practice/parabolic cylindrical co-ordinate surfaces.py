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
    u=np.arange(-1,1,0.01)
    v = np.arange(-1,1,0.01)
    
    X= []
    Y= []
    for i in u:
        for j in v:
            X.append(0.5*(i**2-j**2))
            Y.append(i*j)        
    
    Z = np.full(len(X),2)
    
    graph1 = fig.add_subplot(1,3,1, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.rainbow))


def u_const(fig):    
    z=np.arange(0,1,0.01)
    v = np.arange(-1,1,0.01)
    u=1.0
    X=[]
    Y=[]
    Z=[]
    for i in v:
        for j in z:
            X.append(0.5*(u**2-i**2))
            Y.append(i*u) 
            Z.append(j)
    
    graph1 = fig.add_subplot(1,3,2, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.cool))

def v_const(fig):    
    z= np.arange(0,1,0.01)
    u = np.arange(-1,1,0.01)
    v = 1.0
    
    X=[]
    Y=[]
    Z=[]
    
    for i in u:
        for j in z:
            X.append(0.5*(i**2-v**2))
            Y.append(i*v) 
            Z.append(j)
    
    graph1 = fig.add_subplot(1,3,3, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.coolwarm))

def main():
    fig = plt.figure(figsize=(100,150))
    z_const(fig)
    u_const(fig)
    v_const(fig)
    plt.savefig("Parabolic Cylindrical Co-ordinate surfaces.jpg",dpi=150)

if __name__=="__main__":
    main()
