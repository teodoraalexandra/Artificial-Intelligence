#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:55:07 2020

@author: teodoradan
"""


from itertools import permutations
from prettytable import *
from random import choice


class Particle:
    """ The class that implements a particle """

    def __init__(self, vmin, vmax):
        """ constructor

        input
          vmin: the minimum possible value
          vmax: the maximum possible value
        """
        self.__particle = self.individual(vmin, vmax)
        self.__vmin = vmin
        self.__vmax = vmax

        listPos = []
        for i in range(vmax):
            listPos.append(i)

        self.__position = listPos
        self.__velocity = [0 for i in range(self.__vmax)]

        # the memory of that particle
        self.__bestPosition = self.__position

    def __str__(self):
        p = PrettyTable()
        for row in self.__particle:
            p.add_row(row)
        return p.get_string(header=False, border=False)

    def getVelocity(self):
        return self.__velocity

    def getVelocityByPosition(self, pos):
        return self.__velocity[pos]

    def setVelocityAtPosition(self, pos, newVelocity):
        self.__velocity[pos] = newVelocity

    def getPosition(self):
        return self.__position

    def getPositionByPosition(self, pos):
        return self.__position[pos]

    def setPositionAtPosition(self, pos, newPosition):
        self.__position[pos] = newPosition

    def getBestPosition(self):
        return self.__bestPosition

    def getBestPositionByPosition(self, pos):
        return self.__bestPosition[pos]

    def getElement(self, i, j):
        return self.__particle[i][j]

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

    def shuffleMatrix(self, permutationsList, vmax):
        matrix = [[0 for x in range(vmax)] for y in range(vmax)]
        for row in range(vmax):
            for column in range(vmax):
                element = choice(permutationsList)
                matrix[row][column] = element
                permutationsList.remove(element)
        return matrix

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

    def fitness(self, individual):
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
        suma = (self.__vmax * (self.__vmax + 1)) / 2

        first_row = []
        second_row = []
        for row in range(self.__vmax):
            for column in range(self.__vmax):
                element = individual.getElement(row, column)
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
        for column in range(self.__vmax):
            for row in range(self.__vmax):
                element = individual.getElement(row, column)
                first_column.append(element[0])
                second_column.append(element[1])
            if sum(first_column) == suma:
                f += 1
            if sum(second_column) == suma:
                f += 1
            first_column = []
            second_column = []

        return f
