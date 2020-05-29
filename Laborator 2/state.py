#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:54:35 2020

@author: teodoradan
"""

class State:
    '''
    An array in which we will store possible solutions.
    '''

    def __init__(self):
        self.__values = []

    def addState(self, state):
        self.__values.append(state)

    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]

    def prettyPrint(self):
        for solution in self.__values:
            output = "\n".join(solution)
            print (output + "\n")