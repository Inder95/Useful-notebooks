# -*- coding: utf-8 -*-
"""
Created on Sun May 21 01:01:05 2017

@author: Inderpreet
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:42:15 2017

@author: Inderpreet
"""

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


def phi_const(fig):    
    u=np.arange(-5,5,0.1)
    v = np.arange(-5,5,0.1)
    phi = math.pi/4.0
    X= []
    Y= []
    Z= []
    for i in u:
        for j in v:
            X.append(i*j*math.cos(phi))
            Y.append(i*j*math.sin(phi))        
            Z.append(0.5*(i**2-j**2))
            
    graph1 = fig.add_subplot(1,3,1, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    graph1.set_title("Phi const.")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.rainbow))


def u_const(fig):    
    phi=np.linspace(0,2.0*math.pi,30)
    v = np.arange(-5,5,0.1)
    u=1.0
    X=[]
    Y=[]
    Z=[]
    for i in v:
        for j in phi:
            X.append(i*u*math.cos(j))
            Y.append(i*u*math.sin(j))        
            Z.append(0.5*(u**2-i**2))
    
    graph1 = fig.add_subplot(1,3,2, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    graph1.set_title("U const.")
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.cool))

def v_const(fig):    
    phi=np.linspace(0,2.0*math.pi,30)
    u = np.arange(-5,5,0.1)
    v = 1.0
    X=[]
    Y=[]
    Z=[]
    for i in u:
        for j in phi:
            X.append(i*v*math.cos(j))
            Y.append(i*v*math.sin(j))        
            Z.append(0.5*(i**2-v**2))
    
    graph1 = fig.add_subplot(1,3,3, projection='3d')
    
    graph1.set_zlabel("Z")
    graph1.set_xlabel("X")
    graph1.set_ylabel("Y")
    graph1.set_title("V const.")
    
    #surf1= graph.plot_surface(X,Y,Z,cmap=cm.coolwarm)
    return(graph1.plot_wireframe(X,Y,Z,cmap=cm.coolwarm))
#    return(graph1.plot_trisurf(X,Y,Z,cmap=cm.coolwarm))

def main():
    fig = plt.figure(figsize=(40,10))
    phi_const(fig)
    u_const(fig)
    v_const(fig)
    plt.savefig("Parabolic Co-ordinate surfaces.jpg")

if __name__=="__main__":
    main()