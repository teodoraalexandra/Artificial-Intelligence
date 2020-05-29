#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:06:13 2020

@author: teodoradan
"""


from controller import Controller
from fuzzyDescriptions import FuzzyDescriptions
from fuzzyRule import FuzzyRule


def trapezoidal_region(a, b, c, d):
    #trapezoidal membership function

    return lambda x: max(0, min((x - a) / (b - a), 1, (d - x) / (d - c)))

def triangular_region(a, b, c): 
    #triangular membership function
    
    return trapezoidal_region(a, b, b, c)

def inverse_line(a, b):
    return lambda val: val * (b - a) + a

def inverse_triangular(a, b, c):
    return lambda val: (inverse_line(a, b)(val) + inverse_line(c, b)(val)) / 2


if __name__ == '__main__':
    texture = FuzzyDescriptions()
    capacity = FuzzyDescriptions()
    cycle = FuzzyDescriptions()
    rules = []

    texture.add_region('very soft', trapezoidal_region(-10, 0, 0.2, 0.4))
    texture.add_region('soft', triangular_region(0.2, 0.4, 0.8))
    texture.add_region('normal', triangular_region(0.3, 0.7, 0.9))
    texture.add_region('resistant', trapezoidal_region(0.7, 0.9, 1, 10))

    capacity.add_region('small', trapezoidal_region(-10, 0, 1, 2))
    capacity.add_region('medium', triangular_region(1, 2.5, 4))
    capacity.add_region('high', trapezoidal_region(3, 4, 5, 10))

    cycle.add_region('delicate', trapezoidal_region(-10, 0, 0.2, 0.4), inverse_line(0.4, 0.2))
    cycle.add_region('easy', triangular_region(0.2, 0.5, 0.8), inverse_triangular(0.2, 0.5, 0.8))
    cycle.add_region('normal', triangular_region(0.3, 0.6, 0.9), inverse_triangular(0.2, 0.5, 0.8))
    cycle.add_region('intense', trapezoidal_region(0.7, 0.9, 1, 10), inverse_line(0.7, 0.9))

    #For the washing machine problem, there are 12 rules
    
    rules.append(FuzzyRule({'texture': 'very soft', 'capacity': 'small'},
                           {'cycle': 'delicate'}))
    rules.append(FuzzyRule({'texture': 'very soft', 'capacity': 'medium'},
                           {'cycle': 'easy'}))
    rules.append(FuzzyRule({'texture': 'very soft', 'capacity': 'high'},
                           {'cycle': 'normal'}))
     
    rules.append(FuzzyRule({'texture': 'soft', 'capacity': 'small'},
                           {'cycle': 'easy'}))
    rules.append(FuzzyRule({'texture': 'soft', 'capacity': 'medium'},
                           {'cycle': 'normal'}))
    rules.append(FuzzyRule({'texture': 'soft', 'capacity': 'high'},
                           {'cycle': 'normal'}))
    
    rules.append(FuzzyRule({'texture': 'normal', 'capacity': 'small'},
                           {'cycle': 'easy'}))
    rules.append(FuzzyRule({'texture': 'normal', 'capacity': 'medium'},
                           {'cycle': 'normal'}))
    rules.append(FuzzyRule({'texture': 'normal', 'capacity': 'high'},
                           {'cycle': 'intense'}))
    
    rules.append(FuzzyRule({'texture': 'resistant', 'capacity': 'small'},
                           {'cycle': 'easy'}))
    rules.append(FuzzyRule({'texture': 'resistant', 'capacity': 'medium'},
                           {'cycle': 'normal'}))
    rules.append(FuzzyRule({'texture': 'resistant', 'capacity': 'high'},
                           {'cycle': 'intense'}))

    ctrl = Controller(texture, capacity, cycle, rules)
    
    #Read input data from file
    f = open("input.in", "r")
    texture_input = f.readline()
    capacity_input = f.readline()
    f.close()
     
    print("The input data from the file is: ")
    print("     Texture: " + texture_input)
    print("     Capacity: " + capacity_input)      

    output = ctrl.compute({'texture': float(texture_input), 'capacity': float(capacity_input)})
    print(output)
    
    #Print output data to file
    f = open("output.out", "w")
    f.write(output)
    f.close()
    
    