# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:16:19 2017

@author: Inderpreet
"""

import unittest
from python_practice import simplify_names


class simple_name(unittest.TestCase):
    test_cases=(('this is as</(thest s? )','thisisasthests'),
               ('Kv1.3 ion-channel. ','kvionchannel'),
               ('?the role of amoeb?s','theroleofamoebs'))
    def test_to_simplify(self):
        '''to_simplify should give a string a just alphabets removing \
        special characters, spaces and digits'''
        for i,j in self.test_cases:
            self.assertEqual(j, simplify_names.to_simplify(i))

if __name__=='__main__':
        unittest.main()