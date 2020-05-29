#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:03:41 2020

@author: teodoradan
"""


import random


class Problem:
    def __init__(self, fileName):
        self.fileName = fileName
        self.__testingData = []
        self.__trainingData = []
        self.loadData()

    def loadData(self):
        f = open(self.fileName, "r")
        whole_data = []
        number_of_instances = 0
        for instance in f:
            training_instance = [int(instance[2]), int(instance[4]), int(instance[6]), int(instance[8]), instance[0]]
            whole_data.append(training_instance)
            number_of_instances += 1
        self.manipulateData(whole_data, number_of_instances)

    def manipulateData(self, whole_data, number_of_instances):
        # training_data must be 70% from whole data
        instances_for_training_data = 70 * number_of_instances / 100
        # testing_data will be 30% then
        instances_for_testing_data = number_of_instances - instances_for_training_data

        # choose random some elements for training data
        i = 0
        while i < instances_for_training_data:
            aleatoriu = random.choice(whole_data)
            if aleatoriu not in self.__trainingData:
                self.__trainingData.append(aleatoriu)
                i += 1
            
        for elem in whole_data:
            if elem not in self.__trainingData:
                self.__testingData.append(elem)

    def getTrainingData(self):
        return self.__trainingData

    def getTestingData(self):
        return self.__testingData
