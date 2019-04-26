# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:49:57 2017

@author: Inderpreet
"""

def test_gen():
    global test_t
    test_t += 1
    yield test_t
    
if __name__ == '__main__':
    test_t = 0
    for i in range(5):
        print(next(test_gen()))