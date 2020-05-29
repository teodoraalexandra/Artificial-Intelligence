#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:07:23 2020

@author: teodoradan
"""


class FuzzyDescriptions:
    
    def __init__(self):
        self.regions = {}
        self.inverse = {}

    def add_region(self, var_vame, membership_function, inverse=None):
        self.regions[var_vame] = membership_function
        self.inverse[var_vame] = inverse

    def fuzzify(self, value):
        return {name: membership_function(value)
                for name, membership_function in self.regions.items()
                }

    def defuzzify(self, var_name, value):
        return self.inverse[var_name](value)