# -*- coding: utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math


def z_const(fig):    
    u = np.arange(-5,5,0.1)  
    v = np.arange(-5,5,0.1)
    
    X= []
    Y= []
    for i in u:
        for j in v:
            X.append(math.cosh(i)*math.cos(j))
            Y.append(math.sinh(i)*math.sin(j))   
    
    Z = np.full(len(X),2)
    
    graph1 = fig.add_subplot(1,3,1, projection='3d')
    """ 
    graph1.set_xlim3d(-1,1)
    graph1.set_ylim3d(-1,1)
    graph1.set_zlim3d(-1,1)
    """
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.rainbow))


def u_const(fig):    
    z = np.arange(-5,5,0.1)
    v = np.arange(-5,5,0.1)
    u=1.0
    X=[]
    Y=[]
    Z=[]
    for i in v:
        for j in z:
            X.append(math.cosh(u)*math.cos(i))
            Y.append(math.sinh(u)*math.sin(i))  
            Z.append(j)
    
    graph1 = fig.add_subplot(1,3,2, projection='3d')
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.cool))

def v_const(fig):    
    z= np.arange(-5,5,0.1)
    u = np.arange(-5,5,0.1)
    v = 1.0
    
    X=[]
    Y=[]
    Z=[]
    
    for i in u:
        for j in z:
            X.append(math.cosh(i)*math.cos(v))
            Y.append(math.sinh(i)*math.sin(v))        
            Z.append(j)
    
    graph1 = fig.add_subplot(1,3,3, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.coolwarm))

def main():
    fig = plt.figure(figsize=(40,10))
    z_const(fig)
    u_const(fig)
    v_const(fig)
    plt.savefig("Elliptic Cylindrical Co-ordinate surfaces.jpg")

if __name__=="__main__":
    main()