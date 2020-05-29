#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:09:58 2020

@author: teodoradan
"""


import random


class Problem:
    def __init__(self, fileName):
        self.fileName = fileName
        
        self.X_train = []
        self.X_test = []
        
        self.Y_train = []
        self.Y_test= []
        
        self.Y_train_list = []
        self.Y_test_list = [] 
        
        self.loadData()

    def loadData(self):
        f = open(self.fileName, "r")
        whole_data_x = []
        whole_data_y = []
        x_data_instance = []
        y_data_instance = []
        number_of_instances = 0
        for line in f:
            nums = line.split() # split the line into a list of strings by whitespace
            number_of_instances += 1 
            
            x1 = float(nums[0])
            x2 = float(nums[1])
            x3 = float(nums[2])
            x4 = float(nums[3])
            x5 = float(nums[4])
            
            y = float(nums[5])
            
            x_data_instance = [x1, x2, x3, x4, x5]
            whole_data_x.append(x_data_instance)
            x_data_instance = []
            
            y_data_instance.append(y)
            
        whole_data_y = y_data_instance
        
        self.manipulateData(whole_data_x, whole_data_y, number_of_instances)

    def manipulateData(self, whole_data_x, whole_data_y, number_of_instances):
        # training_data must be 80% from whole data
        instances_for_training_data = round(80 * number_of_instances / 100)
        # testing_data will be 20% then
        instances_for_testing_data = number_of_instances - instances_for_training_data
        
        # choose random some elements for training data
        i = 0
        while i < instances_for_training_data: 
            aleatoriu1 = random.choice(whole_data_x)
            if aleatoriu1 not in self.X_train:
                self.X_train.append(aleatoriu1)
                i += 1
            
        i = 0
        while i < instances_for_training_data:
            aleatoriu2 = random.choice(whole_data_y)
            if aleatoriu2 not in self.Y_train:
                self.Y_train.append(aleatoriu2)
                i += 1
                
        for elem1 in whole_data_x:
            if elem1 not in self.X_train:
                self.X_test.append(elem1)
     
        i = 0
        while i < instances_for_testing_data:
            elem = random.choice(whole_data_y)
            if elem not in self.Y_train:
                self.Y_test.append(elem)
                i += 1
               
        #print(X_train)
        #print("\n")
        #print(X_test)

        self.Y_train_list.append(self.Y_train)
        self.Y_test_list.append(self.Y_test)
        
        #print(Y_train_list)
        #print("\n")
        #hprint(Y_test_list)        

    def getTrainingDataX(self):
        return self.X_train
    
    def getTrainingDataY(self):
        return self.Y_train_list

    def getTestingDataX(self):
        return self.X_test
    
    def getTestingDataY(self):
        return self.Y_test_list
