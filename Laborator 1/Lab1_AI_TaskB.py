# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def menu():
    print("Choose a distribution: ")
    print("0 - exit")
    print("a - uniform") 
    print("b - binomial\n") 
    
def uniform():
    print("Low value: ")
    low = input()
    print("High value: ")
    high = input()
    
    a = np.random.uniform(float(low),float(high),1000)
    count, bins, ignored = plt.hist(a, 15, density = True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()
    
def binomial():
    print("n: ")
    n = input()
    print("p: ")
    p = input()
    b = np.random.binomial(float(n),float(p), 1000)
    count, bins, ignored = plt.hist(b, 15, normed=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()
    
def run():
    menu()
    command = input()
    
    while(command != '0'):
        if command == 'a':
            uniform()
            command = input()
        elif command == 'b':
            binomial()
            command = input()
        else:
            print("Enter your command again: ")

run()
