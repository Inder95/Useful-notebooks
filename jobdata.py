# -*- coding: utf-8 -*-
"""
When we create an instance of class Job with 2 parameters it creates an object with two attributes:
    1.arrival_time
    2.service_time
We use this format to store data during the simulation and also for storing its results.
It makes the program more readable.
 Also this file needs to be in the same directory as you simulation file to run the simulation. 
"""

class Job:
    def __init__(self,arrival_time,service_time):
        self.arrival_time = arrival_time
        self.service_time = service_time
        
