#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:07:00 2020

@author: teodoradan
"""


from fuzzySystem import FuzzySystem


class Controller:
    
    def __init__(self, texture, capacity, cycle, rules):
        #Create the system together with his rules and descriptions
        self.system = FuzzySystem(rules)
        self.system.add_description('texture', texture)
        self.system.add_description('capacity', capacity)
        self.system.add_description('cycle', cycle, out=True) 

    def compute(self, inputs):
        #Call the compute function from self.system
        return "If we have the texture: " + str(inputs['texture']) + \
               " and capacity: " + str(inputs['capacity']) + \
               " we will probably get the cycle type: " + str(self.system.compute(inputs))