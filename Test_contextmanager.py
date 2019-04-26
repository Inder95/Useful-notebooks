# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:10:47 2017

@author: Inderpreet
"""

class Test_contextmanager:
    def __enter__(self):
        print("Entered the contect manager")
    
    def __exit__(self):
        print("Exit the context manager")

if __name__=='__main__':
    import Test_contextmanager as tcm
    with tcm:
        print("Inside the with statement")
    