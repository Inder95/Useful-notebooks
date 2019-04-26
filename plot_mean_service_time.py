# -*- coding: utf-8 -*-
"""
I am storing the result of simulation as a .pickle file. This format is used for storing
Python data objects. You can use this program for plotting simulation results for different seeds
and s by just changing the name of the file where you read from.
"""
import pickle
from matplotlib import pylab as pl

def confidence_interval(t,s):
    mean = sum([i for i in t])/float(len(t))
    std_dev=(sum([(i-mean)**2 for i in t])/float(len(t)*(len(t)-1.0)))**0.5
    print("90% conifdence interval for: ",s," : ", mean - std_dev*1.645, " - ",mean + std_dev*1.645 )
# Reading data from the filename "s_4_seed_0.pickle". Change it to your wish
for p in range(3,11):
    means = []
    for q in [0,10,25,35,50]:
        fname = "s_"+str(p)+"_seed_"+str(q)
        print(fname)
        with open("E:\Java\Python\Simulation log\\"+fname+".pickle",'rb')as f:
            data = pickle.load(f)
        
        x=[]
        y=[]
        
        running_mean = 0
        fig = pl.figure()
        #Iterating through the data to read contents
        for i,j in enumerate(data):
            running_mean = running_mean + j.service_time
            y.append(running_mean/(i+1))
            x.append(j.arrival_time)
        mean = sum([y[k] for k in range(int(len(y)/2),len(y))])/(float(len(y)/2.0))
        means.append(mean)
    
        pl.xlabel("Arrival time")
        pl.ylabel("Mean response time (running)")
        pl.plot(x,y)
        
        #Saving the graph
        pl.savefig(fname+".png")
        pl.clf()
        
    confidence_interval(means,p)