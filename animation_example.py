# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:48:32 2017

@author: Inderpreet
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

fig= plt.figure()
ax = plt.axes(xlim=(0,5), ylim=(-3, +3))
wave, = ax.plot([],[],lw=2)

def init():
    wave.set_data([],[])
    return wave,

def animate(i):
    x=np.linspace(0,10,0.1)
    y=np.sin(2.0*np.pi*(x-0.01*i))
    wave.set_data(x,y)
    return wave,
def iteration():
    for i in range (1000):
        yield i
        
animation= anim.FuncAnimation(fig, animate,iteration, frames=100, interval=20, blit=True, init_func=init)
animation.save('basic_animation.mp4', fps=30)

plt.show()
