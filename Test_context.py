# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:10:47 2017

@author: Inderpreet
"""

class Test_contextmanager:
    def __enter__(self):
        print("Entered the context manager")
    
    def __exit__(self,*args):
        #It is necessary to have *args as the with statement calls the __exit__ method with
        #additional parameters
        print("Exit the context manager")

if __name__=='__main__':
#    import Test_context as tcm
    with Test_contextmanager() :
        print("Inside the with statement")
    
    