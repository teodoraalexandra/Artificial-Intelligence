#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:07:59 2020

@author: teodoradan
"""


class FuzzyRule:
    #For this type of problem we must use the conjunction (min operator)

    def __init__(self, inputs, out):
        self.inputs = inputs
        self.out_var = out 

    def evaluate(self, inputs):
        return [self.out_var, min(
            [inputs[descr_name][var_name]
             for descr_name, var_name in self.inputs.items()
             ])]