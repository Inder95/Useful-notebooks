# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:25:18 2017

@author: Inderpreet
"""

import re

#a = input("Enter the name of the paper")

def to_simplify(name):
    return (''.join(re.findall('[a-z]',name.lower())))
    

if __name__=='__main__':
    print (__name__)
    print(re.__name__)