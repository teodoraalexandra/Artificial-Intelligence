#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:43:26 2020

@author: teodoradan
"""

'''
For a full description:
    
https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6

'''


import numpy as np
import matplotlib as plt
from problem import Problem
from neuralNetwork import NeuralNetwork


if __name__ == "__main__":
    p = Problem("bdate2.txt")
    X_values = p.getX()
    Y_values = p.getY()
    number_of_instances = p.getNumberOfInstances()
    
    #X the array of inputs, Y the array of outputs 
    
    X = np.array(X_values)
    Y = np.array(Y_values)
    neuralNetwork = NeuralNetwork(X, Y, 2)
    
    neuralNetwork.loss = []
    iterations = []
    for i in range(1000): # noOfIterations 
        neuralNetwork.feedforward()
        
        # learning rate = 0.0000001
        neuralNetwork.backprop(0.0000001) 
        
        iterations.append(i)
    
        
    #In this plot we can see how the loss function decreases as iterations increase
    
    plt.pyplot.plot(iterations, neuralNetwork.loss, label='loss value vs iteration')
    plt.pyplot.xlabel('Iterations')
    plt.pyplot.ylabel('loss function')
    plt.pyplot.legend() 
    plt.pyplot.show()
         
    print(neuralNetwork.output)
    
    