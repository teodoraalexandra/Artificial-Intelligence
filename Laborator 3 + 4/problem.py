#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:55:38 2020

@author: teodoradan
"""



from itertools import permutations
from prettytable import *

class Problem:
    def __init__(self, n):
        self.__n = int(n)
        self.__matrix = [['0' for x in range(n)] for y in range(n)]
        self.listOfPermutations = self.computePermutations(1, n)

    def computePermutations(self, vmin, vmax):
        listOfPossibleNumbers = []
        for i in range(vmin, vmax + 1):
            listOfPossibleNumbers.append(i)

        perm = permutations(listOfPossibleNumbers, 2)
        allPermutations = []

        # Compute the arrangements
        for i in list(perm):
            allPermutations.append(i)

        # Add to allPermutations list, the duplicate tuples
        for i in listOfPossibleNumbers:
            miniList = (i, i)
            allPermutations.append(miniList)
        return allPermutations

    def getListOfPermutations(self):
        return self.listOfPermutations

    def getSize(self):
        return self.__n

    def getMatrix(self):
        return self.__matrix

    def setMatrix(self, newMatrix):
        self.__matrix = newMatrix

    def heuristic(self, listOfPermutations, row):
        """
        A heuristic function is a function that will rank all the possible alternatives
        at any branching step in search algorithm based on the available information.
        It helps the algorithm to select the best route out of possible routes.
        *****
        The aim of this function is to arrange the permutations as the first 3 will be correct positioned
        """
        alternative = []
        startNumber = row
        for element in listOfPermutations:
            if len(alternative) == self.getSize():
                break
            if element[0] == startNumber:
                alternative.append(element)
                startNumber += 1
                if startNumber == self.getSize() + 1:
                    startNumber = 1

        for element in listOfPermutations:
            if not alternative.__contains__(element):
                alternative.append(element)

        return alternative

    def expand(self, row_state, listOfPermutations, row):
        listOfPermutations = self.heuristic(listOfPermutations, row)
        for i in range(0, self.getSize()):
            row_state[i] = listOfPermutations[0]
            listOfPermutations.pop(0)

        return row_state, listOfPermutations

    def fitness(self, individual, vmax):
        """
        Determine the fitness of an individual. Higher is better.
        For each individual, which is a matrix, we compute its fitness score
        Fitness score is initially 0.
        As we parse the rows, if numbers are correctly placed, we increase fitness with 1. Maximum here is 2 * vmax
        As we parse the columns, if numbers are correctly placed, we increase fitness with 1. Maximum here is 2 * vmax.
        The optimal solution should have a fitness score of 4 * vmax

        individual: the individual to evaluate
        """
        f = 0
        suma = (vmax * (vmax + 1)) / 2

        first_row = []
        second_row = []
        for row in range(vmax):
            for column in range(vmax):
                element = individual[row][column]
                first_row.append(element[0])
                second_row.append(element[1])
            if sum(first_row) == suma:
                f += 1
            if sum(second_row) == suma:
                f += 1
            first_row = []
            second_row = []

        first_column = []
        second_column = []
        for column in range(vmax):
            for row in range(vmax):
                element = individual[row][column]
                first_column.append(element[0])
                second_column.append(element[1])
            if sum(first_column) == suma:
                f += 1
            if sum(second_column) == suma:
                f += 1
            first_column = []
            second_column = []

        return f

