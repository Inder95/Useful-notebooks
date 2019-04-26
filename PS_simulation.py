# -*- coding: utf-8 -*-
"""
Created on Mon May 22 08:22:34 2017

@author: Inderpreet
"""

import random
import jobdata
import math
import pickle
import time
#This is a generator which generates a new job with its arrival_time and serice_time each time we
#call it.
def job_gen(s):
    #t_gen keeps a track of time
    global t_gen
    #f is clock frequency
    f = 1.25+(0.31*((10.0/s) - 1.0))
    for i in range(s-1):
        t_gen = t_gen + random.expovariate(7.2)*random.uniform(0.75,1.17)
        random.uniform(0.0,gamma)
    t_gen = t_gen + random.expovariate(7.2)*random.uniform(0.75,1.17)
    arrival_time = t_gen
    u = random.uniform(0.0,1) #The upper limit should be 1 not gamma THINK!
    # I will attach the explanation for finding service_time in a separate sheet
    service_time = ((u*(1.0-beta)/gamma)+alpha1**(1-beta))**(1.0/(1.0-beta))
    yield arrival_time,service_time/f

#The following function runs the main simulation
def simulate(s,max_t):
    #We save the first next_departure time and next_arrival time before the loop begins
    job_list = []
    finished_jobs_list = []
    temp_a, temp_b= next(job_gen(s))
    obj= jobdata.Job(temp_a,temp_b)
    t= obj.arrival_time
    next_departure = t + obj.service_time
    job_list.append(obj)
    temp_a, temp_b= next(job_gen(s))
    obj= jobdata.Job(temp_a,temp_b)
    next_arrival = obj.arrival_time
    
    while(t<max_t):
        
        #Arrival Event
        if(next_arrival < next_departure):
            
            for i in job_list:
                if(len(job_list)!=0):
                    i.service_time = i.service_time - ((next_arrival - t)/len(job_list))
                
            job_list.append(obj)
            t = next_arrival
            temp_a, temp_b= next(job_gen(s))
            obj= jobdata.Job(temp_a,temp_b)
            next_arrival = obj.arrival_time
            next_departure = find_next_departure(t,job_list)
    
        #Departure Event
        else:
            for i in job_list:
                if(len(job_list)!=0):
                    i.service_time = i.service_time - ((next_departure - t)/len(job_list)) 
                    
                    if i.service_time <0.1:
                        i.service_time = next_departure - i.arrival_time
                        finished_jobs_list.append(i)
                        job_list.remove(i)
            t = next_departure
            if len(job_list) == 0: 
                job_list.append(obj)
                t = obj.arrival_time
                next_departure = obj.service_time + t
            else:
                next_departure = find_next_departure(t,job_list) 
        print(t)
    return(finished_jobs_list)

#Writes the simulation output to a pickle file. Change the name as per your needs.
def write_to_file(fin_list,s,t):
    fname = "s_"+str(s)+"_seed_"+str(t)+".pickle"            
    with open(fname,'wb') as f:
        pickle.dump(fin_list,f)
    print("s_"+str(s)+"_seed_"+str(t)+".pickle Completed" )
#This functions calculates the next_departure time by finding the job that requires the
#least amout of service time 
def find_next_departure(time, current_jobs):
    return (((min ([i.service_time for i in current_jobs]))*len(current_jobs))+time)
        
              
def main():
    #You can change the values of s and seed here.
    
    s=range(3,11)
    seed = [0,10,25,35,50]
    for i in seed:
        for j in s:
            random.seed(a=i)
            global t_gen
            t_gen=0
            write_to_file(simulate(j, 50000),j,i)
    """
    s=5
    seed=0
    random.seed(a=seed)
    global t_gen
    t_gen=0
    t0= time.time()
    write_to_file(simulate(s, 150000),s,seed)
    print("Minutes taken to execute: ",(time.time()-t0)/60.0)
    """
    
if __name__ =="__main__":
    #Constants from the question
    alpha1= 0.43
    alpha2= 0.98
    beta= 0.86
    gamma= (1.0-beta)/(alpha2**(1-beta)-alpha1**(1-beta))
    main()