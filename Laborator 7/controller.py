#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:14:10 2020

@author: teodoradan
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

class Controller:
    def __init__(self, problem):
        self.problem = problem
        
    def initialize_parameters(self, lenw):
        # we initialize our vector with numbers from normal distribution
        w = np.random.randn(1, lenw)
        
        b = 0
        return w, b

    def forward_prop(self, X, w, b):
        #w ---> 1 x n
        #X ---> n x m 
        
        z = np.dot(w, X) + b
        #z ---> 1 x m
        #b vector = [b b b ...]
        
        return z

    def cost_function(self, z, y):
        m = y.shape[1]
        np.seterr(over='ignore')
        #compute the error
        J = (1/(2*m)) * np.sum((z - y) ** 2)
     
        return np.nan_to_num(J)

    def back_prop(self, X, y, z):
        m = y.shape[1]
        dz = (1/m) * (z-y)
        dw = np.dot(dz, X.T) #dw ---> 1 x n
        db = np.sum(dz)
        
        return dw, db

    def gradient_descent_update(self, w, b, dw, db, learning_rate):
        #as we use gradient descent method, we need to constantly update the coef
        w = w - learning_rate * dw
        b = b - learning_rate * db
        
        return w, b

    def liniar_regression_model(self, X_train, y_train, X_val, y_val, learning_rate, epochs):
        
        lenw = X_train.shape[0]
        w, b = self.initialize_parameters(lenw) #step1
        
        costs_train = []
        errors = []
        m_train = y_train.shape[1]
        m_val = y_val.shape[1]
        
        for i in range(0, epochs):
            z_train = self.forward_prop(X_train, w, b) #step2
            cost_train = self.cost_function(z_train, y_train) #step3
            
            dw, db = self.back_prop(X_train, y_train, z_train) #step4
            
            w, b = self.gradient_descent_update(w, b, dw, db, learning_rate) #step5
            
            #store training cost in a list for plotting purpose
            if i % 10 == 0:
                #only for 10th multiple iterations
                costs_train.append(cost_train)
                
            #MeanAbsoluteError train
            MAE_train = np.nan_to_num((1/m_train) * np.sum(np.abs(z_train - y_train)))
            
            #cost_val, MeanAbsoluteError_val 
            z_val = self.forward_prop(X_val, w, b)
            cost_val = self.cost_function(z_val, y_val)
            MAE_val = np.nan_to_num((1/m_val) * np.sum(np.abs(z_val - y_val)))
            
            #print out cost_train, cost_val, MAE train, MAE val
            
            print ("Epochs " + str(i) + "/" + str(epochs) + ": ")
            print ("Training cost " + str(cost_train) + " | " + "Validation cost " + str(cost_val))
            print ("Training MeanAbsoluteError " + str(MAE_train) + " | " + "Validation MeanAbsoluteError " + str(MAE_val))
            
            computed = MAE_val
            realOutput = MAE_train
            error = computed - realOutput
            errors.append(error)
            
        #if we print all errors, we observe that
        #   in the beginning they aren't that small
        #   but with time whey seem to approach to 0
        #print(errors)
        sum_num = 0
        for t in errors:
            sum_num = sum_num + t           
    
        avg = sum_num / len(errors)
        print ("Final error: ", np.nan_to_num(avg))
        
        self.realTimePlot(costs_train)
        
    def animate_funct(self, x_vals, y_vals, index, costs_train):
        for error in costs_train: 
            x_vals.append(next(index))
            y_vals.append(error)
                
            plt.cla()
            plt.plot(x_vals, y_vals)
            plt.show()
                
    def realTimePlot(self, costs_train):
        plt.style.use('fivethirtyeight')
            
        x_vals = [] 
        y_vals = []
            
        index = count()  
            
        FuncAnimation(plt.gcf(), self.animate_funct(x_vals, y_vals, index, costs_train), interval = 1000)
            
        plt.tight_layout()
        
    def run(self):
        #TRAINING PART
        p = self.problem
        X_train = np.array(p.getTrainingDataX())
        X_train_T = X_train.T
        
        Y_train = np.array(p.getTrainingDataY())
        
        #TESTING PART
        X_val = np.array(p.getTestingDataX())
        X_val_T = X_val.T
        
        Y_val = np.array(p.getTestingDataY())
        
        #PRINTING STUFF
        #print (X_train_T.shape)
        #print (Y_train.shape)
        
        #print (X_val_T.shape)
        #print (Y_val.shape)
        
        self.liniar_regression_model(X_train_T, Y_train, X_val_T, Y_val, 0.4, 500)
        
        
    