# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:17:32 2017

@author: Inderpreet
"""

import pickle

with open("job_log.pickle",'rb') as f:
    data= pickle.load(f)

y = [i.for i in data