# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 00:26:59 2017

@author: Inderpreet
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('ggplot')


dim = 2  #System is 2d (x,y)
nums = 200  #No. of steps
R= np.zeros(dim)
V= np.zeros(dim)
Rs = np.zeros([dim,nums]) # particle position (at all steps)
Vs = np.zeros([dim,nums]) # particle velocity (at all steps)
Et = np.zeros(nums) # total enegy of the system (at all steps)
time = np.zeros(nums) # time (at all steps)
 
def init(): # initialize animation
    particles.set_data([], [])
    line.set_data([], [])
    title.set_text(r'')
    return particles,line,title

def animate(i):
    global R,V,F,Rs,Vs,time,Et
    V = V*(1-zeta/m*dt)-k/m*dt*R # Euler method Eq.(B4)
    R = R + V*dt # Euler method Eq.(B3)
    Rs[0:dim,i]=R
    Vs[0:dim,i]=V
    time[i]=i*dt
    Et[i]=0.5*m*np.linalg.norm(V)**2+0.5*k*np.linalg.norm(R)**2
    particles.set_data(R[0], R[1]) # current position
    line.set_data(Rs[0,0:i], Rs[1,0:i]) # add latest position Rs
    title.set_text(r"$t = {0:.2f},E_T = {1:.3f}$".format(i*dt,Et[i]))
    return particles,line,title

m, k, zeta = 1.0, 1.0, 0.0
# Initial condition
R[0], R[1] = 1., 1. # Rx(0), Ry(0)
V[0], V[1] = 1., 0. # Vx(0), Vy(0)
dt = 0.1*np.sqrt(k/m) # set \Delta t
box = 5 # set size of draw area
fig, ax = plt.subplots(figsize=(7.5,7.5)) # setup plot
ax = plt.axes(xlim=(-box/2,box/2),ylim=(-box/2,box/2)) # draw range
particles, = ax.plot([],[],'ko', ms=10) # setup plot for particle
line,=ax.plot([],[],lw=1) # setup plot for trajectry
title=ax.text(0.5,1.05,r'',transform=ax.transAxes,va='center') # title
anim=animation.FuncAnimation(fig,animate,init_func=init,
frames=nums,interval=5,blit=True,repeat=False) # draw animation
anim.save('SHM.mp4',fps=20)
'''
fig1, ax1 = plt.subplots(figsize=(7.5,7.5))
ax1.set_xlabel(r"$t$", fontsize=20)
ax1.plot(time,Rs[0]) # plot R_x(t)
ax1.plot(time,Rs[1]) # plot R_y(t)
ax1.plot(time,Et) # plot E(t) (ideally constant if \deta=0)
ax1.legend([r'$R_x(t)$',r'$R_y(t)$',r'$E_T(t)$'], fontsize=14)
'''
plt.show()

