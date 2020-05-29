#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:53:05 2020

@author: teodoradan
"""



from random import choice
from itertools import permutations
from prettytable import *


class Chromozome:
    def __init__(self, vmin, vmax):
        self.__chromozome = self.individual(vmin, vmax)
        self.__vmin = vmin
        self.__vmax = vmax

    def outputFormat(self):
        p = PrettyTable()
        for row in self.__chromozome:
            p.add_row(row)
        return p.get_string(header=False, border=False)

    def __len__(self):
        return len(self.__chromozome)

    def setElement(self, i, j, element):
        self.__chromozome[i][j] = element

    def getElement(self, i, j):
        return self.__chromozome[i][j]

    def addMaterial(self, geneticMaterial):
        newIndivid = [[0 for x in range(self.__vmax)] for y in range(self.__vmax)]
        for row in range(self.__vmax):
            for column in range(self.__vmax):
                element = geneticMaterial[row][column]
                newIndivid[row][column] = element
        return newIndivid

    def deleteMaterial(self):
        return [[0 for x in range(self.__vmax)] for y in range(self.__vmax)]

    def individual(self, vmin, vmax):
        """
        Create a member of the population - an individual

        length: the number of genes (components)
        vmin: the minimum possible value
        vmax: the maximum possible value
        """
        permutationList = self.computePermutations(vmin, vmax)
        ind = self.shuffleMatrix(permutationList, vmax)
        return ind

    def computePermutations(self, vmin, vmax):
        """
        The list of permutation we will shuffle later in the individual

        :param vmin: the minimum possible value
        :param vmax: the maximum possible value
        :return: the list of all possible permutations
        """

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

    def shuffleMatrix(self, permutationsList, vmax):
        matrix = [[0 for x in range(vmax)] for y in range(vmax)]
        for row in range(vmax):
            for column in range(vmax):
                element = choice(permutationsList)
                matrix[row][column] = element
                permutationsList.remove(element)
        return matrix
