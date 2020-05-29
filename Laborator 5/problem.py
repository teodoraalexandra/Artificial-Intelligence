#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:07:55 2020

@author: teodoradan
"""


class Problem:
    def __init__(self, data):
        self.__filenameData = data
        self.__matrixSize = self.__loadData()

    def __loadData(self):
        with open(self.__filenameData, 'r') as f2:
            matrixSize = int(f2.readline())

        return matrixSize 

    def getPathLength(self):
        #we compute the solution as a path
        return self.__matrixSize * self.__matrixSize
    
    def getSizeOfMatrix(self):
        return self.__matrixSize