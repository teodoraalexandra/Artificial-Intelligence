#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 18:17:41 2020

@author: teodoradan
"""


import numpy as np


class NeuralNetwork:
    def __init__(self, x, y, hidden):
        self.input      = x
        self.y          = y 
        
        self.weights1   = np.random.rand(5, hidden) 
        self.weights2   = np.random.rand(hidden, 1)           
    
        self.output     = np.zeros(self.y.shape)
        self.loss       = []

    #the activation function (we will use the linear function)
    def linear(self, x):
        return x

    #the derivate of the activation function
    def linear_derivative(self, x):
        return 1

    # the function that computes the output of the network for some input
    def feedforward(self):
        first_cross = np.dot(self.input, self.weights1)
        self.layer1 = self.linear(first_cross)
       
        second_cross = np.dot(self.layer1, self.weights2)
        self.output = self.linear(second_cross)
        
 
    # the backpropagation algorithm 
    def backprop(self, l_rate):
        d_weights1, d_weights2 = [], [] 
        
        delta_r = self.y - self.output
        d_weights2 = np.dot(self.layer1.T, 
                                2 * delta_r * self.linear_derivative(self.output))
           
        delta_h = np.dot(2 * delta_r * self.linear_derivative(self.output), 
                         self.weights2.T * self.linear_derivative(self.layer1))
        d_weights1 = np.dot(self.input.T, delta_h)
                
        # update the weights with the derivative (slope) of the loss function
        self.weights1 += l_rate * d_weights1
        self.weights2 += l_rate * d_weights2 
        
        #Difference between the real output y and the output computed by the network
        loss = self.y - self.output 
        self.loss.append(sum(loss) / len(loss))
            
        