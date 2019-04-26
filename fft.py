# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:48:26 2017

@author: Inderpreet
"""
import math
import numpy as np

def data_gen(f,n):
    data=[]
    for i in range (n):
        data.append(math.cos(i*((2*math.pi/n)*f))+math.sin(i*((2*math.pi/n)*f)))
        #data.append((-1*i*((2*math.pi/n))))
    return(data)

def integral(w,f,n):
    temp=[]
    for i in range (n):
        temp.append(math.sin(i*((2*math.pi/n)*w)))
    temp=np.array(temp)
    data=np.array(data_gen(f,n))
    print("The magnitude of component ",w,"%.2f"%(2*sum([i for i in (temp*data)])/n))
    
def display(f,N):
    data=data_gen(f,N)
    print("Input data:",["%.2f"%dat for dat in data])
    for i in range (N):
        integral(i,f,N)
    print("\nFFT:")
    for i in np.fft.fft(data):    
        print("{0:.2f}".format(i))
    