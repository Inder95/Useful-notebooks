# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:50:02 2017

@author: preet
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(0,10),ylim=(-3,3))

h=1.0
l=10.0
v=2.0

    
x = np.arange(0,l,0.1)
y= [ 2*h*i/l if i<(l/2) else -2*h*i/l+2*h for i in x]

wave, = ax.plot(x,y)

def animate(i):
    wave.set_ydata(fourier(i))
    return wave,
    
def init():
    wave.set_ydata(y)
    return wave,

def fourier(i):
    return (8.0*h*l*(v**-1)*(np.pi**-3))*(np.sin(np.pi*x/l)*np.sin(np.pi*v*i/l)-(1.0/27.0)*
    np.sin(3.0*np.pi*x/l)*np.sin(3.0*np.pi*v*i/l)+(1.0/125.0)*np.sin(5.0*np.pi*x/l)*np.sin(5.0*np.pi*v*i/l))
    

    
ani = animation.FuncAnimation(fig, animate, np.arange(1,50,0.1), init_func=init, blit= True)

ani.save("boas13.4.5.mp4",fps=20)

plt.show()