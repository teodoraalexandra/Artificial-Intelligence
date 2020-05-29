#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:45:35 2020

@author: teodoradan
"""


class Problem:
    def __init__(self, fileName):
        self.fileName = fileName
        
        self.X = []
        self.Y = [] 
        self.Y_list = []
        self.number_of_instances = 0
        
        self.loadData()

    def loadData(self):
        f = open(self.fileName, "r")
        whole_data_x = []
        whole_data_y = []
        x_data_instance = []
        y_data_instance = []
        for line in f:
            nums = line.split() # split the line into a list of strings by whitespace
            self.number_of_instances += 1 
            
            x1 = float(nums[0])
            x2 = float(nums[1])
            x3 = float(nums[2])
            x4 = float(nums[3])
            x5 = float(nums[4])
            
            y = [float(nums[5])]
            
            x_data_instance = [x1, x2, x3, x4, x5]
            whole_data_x.append(x_data_instance)
            x_data_instance = []
            
            y_data_instance.append(y)
            
        whole_data_y = y_data_instance
        
        self.X = whole_data_x
        self.Y = whole_data_y
        
    def getX(self):
        return self.X
    
    def getY(self):
        return self.Y
    
    def getNumberOfInstances(self):
        return self.number_of_instances

    